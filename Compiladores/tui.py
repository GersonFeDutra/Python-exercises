#!/usr/bin/env python3
"""
Rich 2x2 live UI with keyboard-controlled per-pane scrolling.
Demo generator now stops after MAX_GEN lines so you can test interactively.
"""
from typing import Callable, Optional
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.syntax import Syntax
from rich.text import Text
import io
import threading
import time
import sys
import os
import termios
import tty
import select


class Tui:

    class Mode:
        LEXER = 1
        PARSER = 2
        CODE_GEN = 3

    def __init__(self, mode=Mode.CODE_GEN, theme="monokai"):
        self.console = Console()
        self.mode = mode
        self.theme = theme

        # region Buffers
        self.source_buf = io.StringIO()
        self.tokens_buf = io.StringIO()
        self.ir_buf = io.StringIO()
        self.code_buf = io.StringIO()
        self.log_buf = io.StringIO()
        # endregion

        # region State
        # 0: source, 1: tokens, 2: ir, 3: code, 4: log
        self.selected_pane = 0
        self.scroll_offsets = [0] * 5  # number of lines scrolled up (0 = bottom)
        self.lock = threading.Lock()
        self.running = True
        self.need_refresh = True
        self.last_console_size = self.console.size
        # endregion

        # region Widgets (single creation to avoid flicker)
        self.syntax_widget = Syntax(
            "", "c", line_numbers=True, theme="monokai", word_wrap=False
        )
        self.source_panel = Panel(
            self.syntax_widget, title="Source", border_style="cyan"
        )
        self.tokens_panel = Panel("", title="Tokens", border_style="green")
        self.ir_panel = Panel("", title="IR", border_style="yellow")
        self.code_panel = Panel("", title="Codegen", border_style="magenta")
        self.log_panel = Panel("", title="Debug Output", border_style="indian_red")
        # endregion

        # Build initial layout
        self.layout = self.build_layout()

    def build_layout(self):
        """Build or rebuild layout based on current console size"""
        layout = Layout()
        console_height = self.console.size.height

        # Calculate log panel height (25% of console height, minimum 4 lines)
        log_height = max(4, int(console_height * 0.25))

        # Split main area and log panel
        layout.split(
            Layout(name="main", ratio=(console_height - log_height)),
            Layout(name="log", size=log_height),
        )

        # Now split the main area based on mode
        if self.mode == Tui.Mode.LEXER:
            layout["main"].split_row(
                Layout(name="source", ratio=1),
                Layout(name="tokens", ratio=1),
            )
        elif self.mode == Tui.Mode.PARSER:
            layout["main"].split_row(
                Layout(name="source", ratio=1),
                Layout(name="tokens", ratio=1),
                Layout(name="ir", ratio=1),
            )
        else:  # CODE_GEN
            # For code gen, split main area vertically first
            layout["main"].split(
                Layout(name="upper"),
                Layout(name="lower"),
            )
            layout["main"]["upper"].split_row(
                Layout(name="source", ratio=1),
                Layout(name="tokens", ratio=1),
            )
            layout["main"]["lower"].split_row(
                Layout(name="ir", ratio=1),
                Layout(name="code", ratio=1),
            )

        # Assign panels
        layout["source"].update(self.source_panel)
        layout["tokens"].update(self.tokens_panel)

        if self.mode >= Tui.Mode.PARSER:
            layout["ir"].update(self.ir_panel)

        if self.mode >= Tui.Mode.CODE_GEN:
            layout["code"].update(self.code_panel)

        layout["log"].update(self.log_panel)

        return layout

    # region Helpers
    @staticmethod
    def lines_of(text: str) -> list[str]:
        if not text:
            return []
        return text.rstrip("\n").split("\n")

    def compute_visible(self, lines: list[str], pane_height: int, offset: int):
        """
        Given a list of lines, a pane height (usable lines), and a scroll offset,
        return the visible lines (bottom-aligned).
        offset == 0 => show bottom-most lines
        offset > 0 => show older lines (scrolled up)
        """
        usable = max(pane_height - 2, 1)  # reserve for borders/title
        total = len(lines)
        # clamp offset
        offset = max(0, min(offset, max(0, total - usable)))
        # start index for visible slice
        start = max(0, total - usable - offset)
        return lines[start : start + usable], offset

    def render_box(self, name: str, lines_list: list[str], syntax=False):
        # Check if console was resized and rebuild layout if needed
        if self.console.size != self.last_console_size:
            self.layout = self.build_layout()
            self.last_console_size = self.console.size

        # Get layout size for this pane
        try:
            # For nested layouts in CODE_GEN mode
            if self.mode == Tui.Mode.CODE_GEN and name in [
                "source",
                "tokens",
                "ir",
                "code",
            ]:
                if name in ["source", "tokens"]:
                    size = self.layout["main"]["upper"][name].size
                else:
                    size = self.layout["main"]["lower"][name].size
            else:
                size = self.layout[name].size
        except:
            # Fallback for any layout access issues
            size = None

        pane_index = {"source": 0, "tokens": 1, "ir": 2, "code": 3, "log": 4}[name]

        # Calculate pane height
        if size and hasattr(size, "height"):
            height = size.height
        else:
            # Estimate height based on console size and mode
            console_height = self.console.size.height
            if name == "log":
                height = max(4, int(console_height * 0.25))
            elif self.mode == Tui.Mode.CODE_GEN:
                # Half of main area for upper/lower, then split between panes
                main_height = console_height - max(4, int(console_height * 0.25))
                height = max(6, main_height // 2)
            else:
                height = max(10, console_height // 2)

        with self.lock:
            offset: int = self.scroll_offsets[pane_index]

        visible, offset = self.compute_visible(lines_list, height, offset)

        # Update back the clamped offset
        with self.lock:
            self.scroll_offsets[pane_index] = offset

        if syntax:
            content = "\n".join(visible)
            syn = Syntax(content, "c", theme=self.theme, line_numbers=True)
            style = "bold cyan" if self.selected_pane == 0 else "cyan"
            return Panel(syn, title="Source", border_style=style)
        else:
            title = {
                "tokens": "Tokens",
                "ir": "IR",
                "code": "Codegen",
                "log": "Debug Output",
            }[name]
            style_map = {
                "tokens": "green",
                "ir": "yellow",
                "code": "magenta",
                "log": "indian_red",
            }
            idx_map = {"tokens": 1, "ir": 2, "code": 3, "log": 4}
            style = (
                ("bold " + style_map[name])
                if self.selected_pane == idx_map[name]
                else style_map[name]
            )

            # Don't set fixed height on the Panel - let the Layout handle it
            return Panel("\n".join(visible), title=title, border_style=style)

    def render(self):
        # Check for console resize and rebuild layout if needed
        if self.console.size != self.last_console_size:
            self.layout = self.build_layout()
            self.last_console_size = self.console.size

        # Update all panels
        self.layout["source"].update(
            self.render_box(
                "source", self.lines_of(self.source_buf.getvalue()), syntax=True
            )
        )
        self.layout["tokens"].update(
            self.render_box("tokens", self.lines_of(self.tokens_buf.getvalue()))
        )

        if self.mode >= Tui.Mode.PARSER:
            self.layout["ir"].update(
                self.render_box("ir", self.lines_of(self.ir_buf.getvalue()))
            )
            self.layout["log"].update(
                self.render_box("log", self.lines_of(self.log_buf.getvalue()))
            )

        if self.mode >= Tui.Mode.CODE_GEN:
            self.layout["code"].update(
                self.render_box("code", self.lines_of(self.code_buf.getvalue()))
            )

        return self.layout

    # endregion

    # region API used by your compiler to append data
    def log_source(self, line: str, end="\n", flush=True):
        with self.lock:
            self.source_buf.write(f"{line}{end}")
            self.scroll_offsets[0] = 0
        if flush:
            self.update()
        else:
            self.mark_refresh()

    def log_tokens(self, line: str = "", end="\n", flush=True):
        with self.lock:
            self.tokens_buf.write(f"{line}{end}")
            self.scroll_offsets[1] = 0
        if flush:
            self.update()
        else:
            self.mark_refresh()

    def log_ir(self, line: str, end="\n", flush=True):
        with self.lock:
            self.ir_buf.write(f"{line}{end}")
            self.scroll_offsets[2] = 0
        if flush:
            self.update()
        else:
            self.mark_refresh()

    def log_code(self, line: str, end="\n", flush=True):
        with self.lock:
            self.code_buf.write(f"{line}{end}")
            self.scroll_offsets[3] = 0
        if flush:
            self.update()
        else:
            self.mark_refresh()

    def log_debug(self, line: str, end="\n", flush=True):
        with self.lock:
            self.log_buf.write(f"{line}{end}")
            self.scroll_offsets[4] = 0
        if flush:
            self.update()
        else:
            self.mark_refresh()

    def mark_refresh(self):
        with self.lock:
            self.need_refresh = True

    # endregion

    def update(self):
        if self._live is not None:
            self._live.update(self.render())

    def input_thread(self):
        """Input handling thread (keyboard only)"""
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)  # allow signals (Ctrl-C) but read raw input
            while self.running:
                r, _, _ = select.select([fd], [], [], 0.1)
                if not r:
                    continue
                data = os.read(fd, 32)  # read up to 32 bytes
                if not data:
                    continue
                try:
                    s = data.decode("utf-8", "ignore")
                except:
                    s = ""
                if s in ("q", "\x03"):  # q or Ctrl-C
                    self.running = False
                    break
                if s in ("1", "2", "3", "4", "5"):
                    self.selected_pane = int(s) - 1
                    self.mark_refresh()
                    continue
                # j/k and arrows
                if s in ("j", "\x1b[B"):  # down (newer)
                    with self.lock:
                        self.scroll_offsets[self.selected_pane] = max(
                            0, self.scroll_offsets[self.selected_pane] - 1
                        )
                    self.mark_refresh()
                    continue
                if s in ("k", "\x1b[A"):  # up (older)
                    with self.lock:
                        self.scroll_offsets[self.selected_pane] += 1
                    self.mark_refresh()
                    continue
                if s in ("J", "\x1b[1;2B"):  # shift + down (newer)
                    with self.lock:
                        for i, offset in enumerate(self.scroll_offsets):
                            self.scroll_offsets[i] = max(0, offset - 1)
                    self.mark_refresh()
                    continue
                if s in ("K", "\x1b[1;2A"):  # shift + up (older)
                    with self.lock:
                        for i, offset in enumerate(self.scroll_offsets):
                            self.scroll_offsets[i] += 1
                    self.mark_refresh()
                    continue
                if s == "u":  # page up (older)
                    with self.lock:
                        self.scroll_offsets[self.selected_pane] += 10
                    self.mark_refresh()
                    continue
                if s == "d":  # page down (newer)
                    with self.lock:
                        self.scroll_offsets[self.selected_pane] = max(
                            0, self.scroll_offsets[self.selected_pane] - 10
                        )
                    self.mark_refresh()
                    continue
                if s == "g":  # go top
                    with self.lock:
                        name = ["source", "tokens", "ir", "code", "log"][
                            self.selected_pane
                        ]
                        lines = (
                            {
                                "source": self.source_buf,
                                "tokens": self.tokens_buf,
                                "ir": self.ir_buf,
                                "code": self.code_buf,
                                "log": self.log_buf,
                            }[name]
                            .getvalue()
                            .splitlines()
                        )
                        size = self.console.size
                        # Estimate pane height based on console size and mode
                        if name == "log":
                            h = max(4, int(size.height * 0.25))
                        elif self.mode == Tui.Mode.CODE_GEN and name in [
                            "source",
                            "tokens",
                            "ir",
                            "code",
                        ]:
                            main_height = size.height - max(4, int(size.height * 0.25))
                            h = max(6, main_height // 2)
                        else:
                            h = max(10, size.height // 2)
                        usable = max(h - 2, 1)
                        max_off = max(0, len(lines) - usable)
                        self.scroll_offsets[self.selected_pane] = max_off
                    self.mark_refresh()
                    continue
                if s == "G":  # go bottom
                    with self.lock:
                        self.scroll_offsets[self.selected_pane] = 0
                    self.mark_refresh()
                    continue
                # ignore other keys
        finally:
            try:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            except Exception:
                pass

    def _run(self, task: Callable[[], None], hold: bool):
        """Live loop + controlled generator"""

        # start input reader
        t = threading.Thread(target=self.input_thread, daemon=True)
        last_update_time = time.time()
        t.start()

        with Live(
            self.render(), console=self.console, refresh_per_second=20, screen=True
        ) as live:
            self._live = live
            task()

            self.running = hold
            # Holds the process after task run.
            while self.running:
                # refresh UI only when needed (efficient)
                if self.need_refresh or (time.time() - last_update_time) > 0.1:
                    with self.lock:
                        self.need_refresh = False
                    self.update()
                    last_update_time = time.time()

                time.sleep(0.03)  # keep UI responsive, tune as needed

        self.running = False
        t.join(timeout=0.2)

    def run(self, task: Callable[[], None], hold=False):
        try:
            self._run(task, hold)
        except KeyboardInterrupt:
            self.running = False
            print("\nExiting.", file=sys.stderr)


if __name__ == "__main__":
    ui = Tui()

    def f():
        # Demo generator limit
        MAX_GEN = 100  # number of demo lines to generate (change to suit)
        count = 0
        last_update_time = time.time()
        generation_finished = False

        while ui.running:
            # generate only up to MAX_GEN
            if count < MAX_GEN:
                ui.log_source(f"int x{count} = {count};")
                ui.log_tokens(f"TOKEN NUM {count}")
                ui.log_ir(f"(Assign x{count} {count})")
                ui.log_code(f"t{count} = {count}")
                ui.log_debug(f"Generated line {count}")
                count += 1
            elif not generation_finished:
                # mark finished and write a status line
                ui.log_code(
                    f"--- generation finished ({MAX_GEN} lines). Press 'q' to quit ---"
                )
                generation_finished = True

            # refresh UI only when needed (efficient)
            if ui.need_refresh or (time.time() - last_update_time) > 0.1:
                with ui.lock:
                    ui.need_refresh = False
                ui.update()
                last_update_time = time.time()

            time.sleep(0.03)  # keep UI responsive, tune as needed

    ui.run(f)

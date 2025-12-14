#!/usr/bin/env python3
"""
Rich 2x2 live UI with keyboard-controlled per-pane scrolling.
Demo generator now stops after MAX_GEN lines so you can test interactively.
"""
from typing import Optional
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


console = Console()

#region Buffers
source_buf = io.StringIO()
tokens_buf = io.StringIO()
ir_buf     = io.StringIO()
code_buf   = io.StringIO()
#endregion

#region State
# 0: source, 1: tokens, 2: ir, 3: code
selected_pane = 0
scroll_offsets = [0, 0, 0, 0]  # number of lines scrolled up (0 = bottom)
lock = threading.Lock()
running = True
need_refresh = True
#endregion

# Demo generator limit
MAX_GEN = 100  # number of demo lines to generate (change to suit)

#region Widgets (single creation to avoid flicker)
syntax_widget = Syntax('', 'c', line_numbers=True, theme='monokai', word_wrap=False)
source_panel = Panel(syntax_widget, title='Source', border_style='cyan')
tokens_panel = Panel('', title='Tokens', border_style='green')
ir_panel     = Panel('', title='IR', border_style='yellow')
code_panel   = Panel('', title='Codegen', border_style='magenta')
#endregion


#region Layout
def build_layout():
    layout = Layout()
    layout.split(
        Layout(name='top'),
        Layout(name='bottom'),
    )
    layout['top'].split_row(
        Layout(name='source'),
        Layout(name='tokens'),
    )
    layout['bottom'].split_row(
        Layout(name='ir'),
        Layout(name='code'),
    )
    
    # assign panels once (placeholders)
    layout['source'].update(source_panel)
    layout['tokens'].update(tokens_panel)
    layout['ir'].update(ir_panel)
    layout['code'].update(code_panel)
    return layout


layout: Layout = build_layout()
#endregion


#region Helpers
def lines_of(text: str):
    if not text:
        return []
    return text.rstrip('\n').split('\n')


def compute_visible(lines, pane_height, offset):
    '''
    Given a list of lines, a pane height (usable lines), and a scroll offset,
    return the visible lines (bottom-aligned).
    offset == 0 => show bottom-most lines
    offset > 0 => show older lines (scrolled up)
    '''
    usable = max(pane_height - 2, 1)  # reserve for borders/title
    total = len(lines)
    # clamp offset
    offset = max(0, min(offset, max(0, total - usable)))
    # start index for visible slice
    start = max(0, total - usable - offset)
    return lines[start:start + usable], offset


def render_box(name, lines_list, syntax=False):
    # If layout size unknown (first frames), supply safe fallback
    size = layout[name].size
    height = size.height if size and size.height else 20 # type: ignore
    pane_index = {'source':0,'tokens':1,'ir':2,'code':3}[name]
    with lock:
        offset = scroll_offsets[pane_index]
    visible, offset = compute_visible(lines_list, height, offset)
    # update back the clamped offset
    with lock:
        scroll_offsets[pane_index] = offset
    
    if syntax:
        content = '\n'.join(visible)
        syn = Syntax(content, 'c', theme='monokai', line_numbers=True)
        style = 'bold cyan' if selected_pane == 0 else 'cyan'
        return Panel(syn, title='Source', border_style=style)
    else:
        title = {'tokens': 'Tokens', 'ir': 'IR','code': 'Codegen'}[name]
        style_map = {'tokens': 'green', 'ir': 'yellow', 'code': 'magenta'}
        idx_map = {'tokens': 1,'ir': 2,'code': 3}
        style = ('bold ' + style_map[name]) if selected_pane == idx_map[name] else style_map[name]
        return Panel('\n'.join(visible), title=title, border_style=style)


def render():
    # Read current buffer contents and render panels using current scroll offsets
    layout['source'].update(render_box('source', lines_of(source_buf.getvalue()), syntax=True))
    layout['tokens'].update(render_box('tokens', lines_of(tokens_buf.getvalue())))
    layout['ir'].update(render_box('ir', lines_of(ir_buf.getvalue())))
    layout['code'].update(render_box('code', lines_of(code_buf.getvalue())))
    return layout
#endregion


#region API used by your compiler to append data
def log_source(line):
    with lock:
        source_buf.write(line + "\n")
        scroll_offsets[0] = 0
    mark_refresh()


def log_tokens(line):
    with lock:
        tokens_buf.write(line + "\n")
        scroll_offsets[1] = 0
    mark_refresh()


def log_ir(line):
    with lock:
        ir_buf.write(line + "\n")
        scroll_offsets[2] = 0
    mark_refresh()


def log_code(line):
    with lock:
        code_buf.write(line + "\n")
        scroll_offsets[3] = 0
    mark_refresh()


def mark_refresh():
    global need_refresh
    with lock:
        need_refresh = True
#endregion


#region Input handling thread (keyboard only)
def input_thread():
    global running, selected_pane, need_refresh
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)  # allow signals (Ctrl-C) but read raw input
        while running:
            r, _, _ = select.select([fd], [], [], 0.1)
            if not r:
                continue
            data = os.read(fd, 32)  # read up to 32 bytes
            if not data:
                continue
            try:
                s = data.decode('utf-8', 'ignore')
            except:
                s = ''
            if s in ('q', '\x03'):  # q or Ctrl-C
                running = False
                break
            if s in ('1','2','3','4'):
                selected_pane = int(s) - 1
                mark_refresh()
                continue
            # j/k and arrows
            if s in ('j', '\x1b[B'):  # down (newer)
                with lock:
                    scroll_offsets[selected_pane] = max(0, scroll_offsets[selected_pane] - 1)
                mark_refresh()
                continue
            if s in ('k', '\x1b[A'):  # up (older)
                with lock:
                    scroll_offsets[selected_pane] += 1
                mark_refresh()
                continue
            if s == 'u':  # page up (older)
                with lock:
                    scroll_offsets[selected_pane] += 10
                mark_refresh()
                continue
            if s == 'd':  # page down (newer)
                with lock:
                    scroll_offsets[selected_pane] = max(0, scroll_offsets[selected_pane] - 10)
                mark_refresh()
                continue
            if s == 'g':  # go top
                with lock:
                    name = ['source', 'tokens', 'ir', 'code'][selected_pane]
                    lines = {
                        'source': source_buf,'tokens': tokens_buf, 'ir': ir_buf, 'code': code_buf
                    }[name].getvalue().splitlines()
                    size = layout[name].size
                    h = size.height if size and size.height else 20 # type: ignore
                    usable = max(h - 2, 1)
                    max_off = max(0, len(lines) - usable)
                    scroll_offsets[selected_pane] = max_off
                mark_refresh()
                continue
            if s == 'G':  # go bottom
                with lock:
                    scroll_offsets[selected_pane] = 0
                mark_refresh()
                continue
            # ignore other keys
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        except Exception:
            pass
#endregion


#region Main: Live loop + controlled generator
def main():
    global running, need_refresh
    # start input reader
    t = threading.Thread(target=input_thread, daemon=True)
    t.start()
    
    with Live(render(), console=console, refresh_per_second=20, screen=True) as live:
        count = 0
        last_update_time = time.time()
        generation_finished = False
        
        while running:
            # generate only up to MAX_GEN
            if count < MAX_GEN:
                log_source(f'int x{count} = {count};')
                log_tokens(f'TOKEN NUM {count}')
                log_ir(f'(Assign x{count} {count})')
                log_code(f't{count} = {count}')
                count += 1
            elif not generation_finished:
                # mark finished and write a status line
                log_code(f"--- generation finished ({MAX_GEN} lines). Press 'q' to quit ---")
                generation_finished = True
            
            # refresh UI only when needed (efficient)
            if need_refresh or (time.time() - last_update_time) > 0.1:
                with lock:
                    need_refresh = False
                live.update(render())
                last_update_time = time.time()
            
            time.sleep(0.03)  # keep UI responsive, tune as needed
    
    running = False
    t.join(timeout=0.2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        running = False
        print('\nExiting.')
#endregion

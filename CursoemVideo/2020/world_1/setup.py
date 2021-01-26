import sys
from cx_Freeze import setup, Executable
# includes below
import pygame
import colorama

# No terminal
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

# executables = [
#         Executable("script.py", base=base)
# ]

# With terminal
executables = [
        Executable("ex001.py", base=None)
]

buildOptions = dict(
        packages = [],
        includes = ['pygame', 'colorama'],
        include_files = ['hello_world.mp3'],
        excludes = []
)

setup(
    name = "Hello World",
    version = "1.0",
    description = "Let's sing.",
    options = dict(build_exe = buildOptions),
    executables = executables
 )

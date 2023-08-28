import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "IFE Application",
    version = "1.0.0",
    description = "A Video Processing Software Application",
    author = "Farruck Ahamed Tusar",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
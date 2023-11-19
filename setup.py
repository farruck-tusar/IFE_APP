import sys
from cx_Freeze import setup, Executable

sys.setrecursionlimit(10000)

build_exe_options = {
    "packages": ["PySide6", "numpy", "yolov5", "torch", "ultralytics", "seaborn"],
    "excludes": [],
    "zip_include_packages": [],
}

target = Executable(
    script="main.py",
    base = "Win32GUI" if sys.platform == "win32" else None,
    icon="resources/icon.ico"
)

setup(
    name = "IFE Application",
    version = "1.0.0",
    description = "A Video Processing Software Application",
    author = "Farruck Ahamed Tusar",
    options={"build_exe": build_exe_options},
    executables = [target]
)

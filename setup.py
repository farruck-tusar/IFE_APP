import sys
from cx_Freeze import setup, Executable

sys.setrecursionlimit(10000)

build_exe_options = {
    "packages": ["PySide6", "numpy", "yolov5", "torch", "ultralytics", "seaborn"],
    "excludes": [],
    "zip_include_packages": [],
}

directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program"),
]

msi_data = {
    "Directory": directory_table,
    "ProgId": [
        ("Prog.Id", None, None, "This is a description", "IconId", None),
    ],
    "Icon": [
        ("IconId", "resources/icon.ico"),
    ],
}

bdist_msi_options = {
    "add_to_path": True,
    "data": msi_data
}

bdist_dmg_options = {

}

executables = [
    Executable(
        script="main.py",
        copyright="Copyright (C) 2023 TUC",
        base="Win32GUI" if sys.platform == "win32" else None,
        icon="resources/icon.ico",
        shortcut_name="IFE",
        shortcut_dir="MyProgramMenu",
    )
]

setup(
    name = "IFE Application",
    version = "1.0.0",
    description = "A Video Processing Software Application",
    author = "Farruck Ahamed Tusar",
    executables = executables,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
        "bdist_dmg": bdist_dmg_options,
    }
)

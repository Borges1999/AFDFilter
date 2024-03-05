import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "includes": ["tkinter", "tkcalendar", "customtkinter"],
    "zip_include_packages": ["encodings", "PySide6"],
    "include_files": ["filtro.ico", "clips.svg", "lixeira.svg"]    
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="AFDFilter",
    version="2.0",
    description="AFDFilter",
    options={"build_exe": build_exe_options},
    executables=[Executable("afdfilter.py", base=base, icon="filtro.ico")],
)
from cx_Freeze import setup, Executable
import sys

# Nombre del archivo principal
main_script = "carga_productos.py"

# Configuración de opciones
build_exe_options = {
    "packages": [
        "os", "sys", "pandas", "openpyxl", "escpos", "csv", "PyQt5"
    ],
    "excludes": [],
    "include_files": [],
    "include_msvcr": True,  # incluye runtime de Visual C++
}

# Evitar error 'QmlImportsPath' (bug de cx_Freeze con PyQt)
import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = ""
os.environ["QT_PLUGIN_PATH"] = ""

setup(
    name="Tickeadora",
    version="1.0",
    description="App de Tickeadora con PyQt5",
    options={"build_exe": build_exe_options},
    executables=[Executable(main_script, base="Win32GUI")]
)


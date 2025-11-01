from cx_Freeze import setup, Executable

# Opciones de compilación
build_exe_options = {
    "packages": [
        "os", "sys", "openpyxl", "pandas", "csv", "datetime",
        "PyQt5", "escpos", "usb", "collections"
    ],
    "include_files": [],
    "include_msvcr": True,  # incluye las DLL de Visual C++
}

# Configuración del ejecutable
setup(
    name="Tickeadora",
    version="1.0",
    description="Aplicación de tickeadora para control de ventas",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("main.py", base="Win32GUI", target_name="Tickeadora.exe")
    ]
)

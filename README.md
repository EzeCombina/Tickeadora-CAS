# Tickeadora-CAS

## Pasos a seguir para la puesta a punto de la app:

### Descargar python en el sistema desde la página oficial. 

### Descargar VSCode. 

### Descargar librerias necesarias. 

## Librerias necesarias: 

### pip install pyqt5 openpyxl pandas python-escpos pyusb pillow cx_Freeze (Correr desde la terminal propia de VSCode).

### IMPORTANTE: Tener actualizado pip.

## Drivers de la impresora: 

### Descargar Zadig 2.9

### Ir a opciones y a listar todos los dispositivos. 

### Seleccionar libusbK (v3.1.0.0) y darle a Replace Driver o Install Driver. 

## CX_Freeze para generar el ejecutable: 

### Abrir cmd, ir a la carpeta donde esta main.py y ejecutar el siguiente comando:

### cxfreeze main.py --target-dir dist

## En caso de que cxfreeze no funcione.. Usar pyinstaller con los siguientes comandos: 

### pip install pyinstaller

### pyinstaller --noconsole --onefile --add-data "C:\Users\""USUARIO""\AppData\Local\Programs\Python\Python313\Lib\site-packages\escpos\capabilities.json;escpos" main.py
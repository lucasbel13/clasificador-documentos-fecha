Descripción
Este proyecto es una herramienta en Python que organiza archivos según su fecha de modificación (o creación) moviéndolos a subcarpetas organizadas por año y mes. Es especialmente útil para archivar documentos antiguos y mantener organizados los nuevos, facilitando la gestión y búsqueda de archivos en tu sistema.

Herramientas y Funcionalidades
Python: Lenguaje de programación utilizado para desarrollar la herramienta.
Módulos de la Biblioteca Estándar:
os: Para manejar rutas y obtener información del sistema.
shutil: Para mover archivos.
datetime: Para convertir timestamps a fechas legibles.
Función Principal: Extraer la fecha de modificación o creación de cada archivo y moverlo a una carpeta con la estructura Año/Mes dentro de la carpeta origen.
Requisitos
Python 3.x (se recomienda la versión 3.7 o superior).
Sistema operativo que permita mover archivos (Windows, Linux o macOS).
Nota: No se requieren dependencias externas, ya que se utilizan únicamente módulos de la biblioteca estándar de Python.

Instalación y Uso
Instalación
Clonar o descargar el repositorio:
Si usas Git, ejecuta:
bash

git clone <URL_DEL_REPOSITORIO>
Navega a la carpeta del proyecto:
bash

cd <NOMBRE_DEL_PROYECTO>
Uso
Ejecuta el script desde la línea de comandos:
bash

python Clasificador_de_archivos.py
Ingresa la ruta de la carpeta que contiene los archivos que deseas clasificar cuando se te solicite.
El script procesará cada archivo, moviéndolo a la subcarpeta correspondiente según su año y mes de modificación (o creación).

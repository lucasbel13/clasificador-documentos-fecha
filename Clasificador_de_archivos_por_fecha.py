import os
import shutil
import datetime

# Diccionario para convertir el número del mes a su nombre en español.
MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

def obtener_fecha_archivo(ruta_archivo):
    """
    Retorna la fecha de modificación del archivo como objeto datetime.
    En Windows, os.path.getctime devuelve la fecha de creación; en otros sistemas se puede usar la fecha de modificación.
    """
    try:
        # Puedes cambiar getmtime por getctime si prefieres la fecha de creación.
        timestamp = os.path.getmtime(ruta_archivo)
        return datetime.datetime.fromtimestamp(timestamp)
    except Exception as e:
        print(f"Error al obtener la fecha del archivo {ruta_archivo}: {e}")
        return None

def clasificar_por_fecha(carpeta):
    """
    Recorre los archivos de la carpeta indicada y los mueve a subcarpetas según el año y mes de su fecha de modificación.
    """
    # Listar los archivos (solo los que son archivos, ignoramos carpetas)
    archivos = [archivo for archivo in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, archivo))]
    
    if not archivos:
        print("No se encontraron archivos en la carpeta indicada.")
        return
    
    total = len(archivos)
    print(f"Se encontraron {total} archivo(s) en la carpeta '{carpeta}'.")
    
    for indice, archivo in enumerate(archivos, start=1):
        ruta_archivo = os.path.join(carpeta, archivo)
        fecha = obtener_fecha_archivo(ruta_archivo)
        if fecha is None:
            print(f"No se pudo obtener la fecha para {archivo}.")
            continue
        
        anio = str(fecha.year)
        mes = MESES.get(fecha.month, str(fecha.month))
        
        # Crear la ruta de destino: Carpeta/Anio/Mes
        ruta_destino = os.path.join(carpeta, anio, mes)
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)
        
        nueva_ruta = os.path.join(ruta_destino, archivo)
        try:
            shutil.move(ruta_archivo, nueva_ruta)
            print(f"[{indice}/{total}] Archivo '{archivo}' movido a: {nueva_ruta}")
        except Exception as e:
            print(f"Error al mover el archivo {archivo}: {e}")

if __name__ == "__main__":
    carpeta = input("Ingresa la ruta de la carpeta que contiene los archivos: ").strip()
    if os.path.isdir(carpeta):
        clasificar_por_fecha(carpeta)
        print("\nClasificación por fecha completada.")
    else:
        print("La ruta proporcionada no es una carpeta válida.")

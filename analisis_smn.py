import os
import sys
import Funciones_smn as fc

def main() -> None:
    """Función principal para validar argumentos y ejecutar el análisis SMN."""
    
    if len(sys.argv) < 2:
        print("Error: Falta indicar la ruta del archivo de datos.")
        print("Uso correcto: python analisis_smn.py datos/observaciones_smn.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]

    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        sys.exit(1)

    
    if os.path.getsize(ruta_archivo) == 0:
        print(f"Error: El archivo '{ruta_archivo}' está vacío.")
        sys.exit(1)

    
    reporte = {"lineas_invalidas": 0, "columnas_ausentes": 0}
    try:
        observaciones = fc.leer_observaciones(ruta_archivo, reporte)
    except Exception as error:
        print(f"Error al procesar el archivo: {error}")
        sys.exit(1)

    
    if not observaciones:
        print(f"Error: No se encontró ninguna observación válida en '{ruta_archivo}'.")
        sys.exit(1)

    
    fc.mostrar_resumen(
    observaciones,
    reporte.get("lineas_invalidas", 0),
    reporte.get("columnas_ausentes", 0)
    )

if __name__ == "__main__":
    main()



        

        
    

        

    


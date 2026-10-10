import os
import sys
import json 
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

    if ruta_archivo.endswith('.txt'):

        try:
            lectura = fc.toconvert_file_tojson(fc.to_verify_file(ruta_archivo))
            mi_json = json.dumps(lectura, ensure_ascii=False, indent=4)
            print(mi_json )
            namejson = os.path.basename(ruta_archivo).replace('.txt', '.json')
            exit_way = os.path.join('obs_json', namejson)

            os.makedirs('obs_json', exist_ok=True)

            with open(exit_way, 'w', encoding='utf-8') as f:
                f.write(mi_json)

        except Exception as error:
            print(f"Error al procesar el archivo: {error}")
            sys.exit(1)


if __name__ == "__main__":
    main()
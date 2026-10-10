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

    if ruta_archivo.endswith('.txt'):
        print("\nArchivo del SMN (.txt) detectado, convirtiendo a JSON...")

    try:
        # 1. Lectura y procesamiento
        raw_content = fc.to_verify_file(ruta_archivo)
        lectura = fc.toconvert_file_tojson(raw_content)
        mi_json = json.dumps(lectura, ensure_ascii=False, indent=4)

        output_dir = 'obs_json'

        # 2. Verificación de carpeta
        if not os.path.exists(output_dir):
            print(f"No se localizó la carpeta '{output_dir}', procediendo a generarla...")
            os.makedirs(output_dir, exist_ok=True)
            print(f"Directorio '{output_dir}' creado con éxito.\n")
        else:
            print(f"\nLa carpeta '{output_dir}' se encuentra disponible en el sistema.\n")

        # 3. Guardado
        namejson = os.path.basename(ruta_archivo).replace('.txt', '.json')
        exit_way = os.path.join(output_dir, namejson)

        print(f"Guardando archivo en '{exit_way}'...")
        with open(exit_way, 'w', encoding='utf-8') as f:
            f.write(mi_json)
        print("\nArchivo JSON guardado con éxito.\n")

        # 4. Resumen final (exactamente 2 líneas)
        total_cities = len([linea for linea in raw_content.splitlines() if linea.strip()])
        reported_cities = len(lectura)

        print(f"Registros de localidades detectados en el archivo: {total_cities}")
        print(f"Localidades con reporte meteorológico válido: {reported_cities}\n")

    except Exception as error:
        print(f"\nError al procesar el archivo: {error}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
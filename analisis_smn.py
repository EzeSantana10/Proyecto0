import sys

from Funciones_smn import leer_observaciones, cantidad_ciudades, ciudades_completas, horarios_reportados, mostrar_resumen

campos_esperados = [
    "ciudad", "fecha y hora", "condicion", "visibilidad", "temperatura", 
    "sensacion termica", "humedad", "viento", "presion",
]

def main():

    if len(sys.argv) != 2:
        sys.exit("python analsis_smn archivo_observaciones.txt")

    archivo = sys.argv[1]

    try:
        observaciones = leer_observaciones(archivo)
    except FileNotFoundError:
        sys.exit("No se pudieron leer observaciones validas.")
    
if __name__ == "__main__":
    def()



        

        
    

        

    


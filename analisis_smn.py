import sys

if len(sys.argv) < 2:
    print("La cantidad de argumentos ingresados es menor a la esperada")
    sys.exit()

archivo = sys.argv[1]
diccionario = {}

with open (archivo, "r", encoding="cp1252") as file:
    next(file)

    for linea in file:
        linea_limpia = linea.strip()
        columnas = linea_limpia.split(";")
        ciudad = columnas[0]
        viento_sin_parsear = columnas[8].strip()
        componentes = viento_sin_parsear.split()

        if len(componentes) >= 2:
            direccion_viento = componentes[0]

            try:
                velocidad_viento = float(componentes[1])
            except ValueError:
                velocidad_viento = 0 
                
        else:
            direccion_viento = viento_sin_parsear.strip() 
            velocidad_viento = 0

        diccionario[ciudad] = {
            "fecha": columnas[1].strip(),
            "hora": columnas[2].strip(),
            "condicion": columnas[3].strip(),
            "visibilidad": columnas[4].strip(),
            "temperatura": columnas[5].strip(),
            "sensacion_termica": columnas[6].strip(),
            "humedad": columnas[7].strip(),
            "direccion_viento": direccion_viento,
            "velocidad_viento": velocidad_viento,
            "presion": columnas[9].strip()
        }



        

        
    

        

    


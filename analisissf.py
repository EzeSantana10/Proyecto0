dato_limpio = []
diccionario_datos = {
    "Ciudad/Estación": [],
    "Fecha": [],
    "Hora": [],
    "Condición del cielo": [],
    "Visibilidad": [],
    "Temperatura": [],
    "Sensación térmica": [],
    "Humedad": [],
    "Viento": [],
    "Presión": []
}

with open ("estado_tiempo20260910.txt", "r", encoding="cp1252") as archivo:

    for linea in archivo:
        linea1 = linea.strip("\n")
        columnas = linea1.split(";")
        dato_limpio.append(columnas)

    for datos in dato_limpio:
        diccionario_datos["Ciudad/Estación"].append(datos[0])
        diccionario_datos["Fecha"].append(datos[1])
        diccionario_datos["Hora"].append(datos[2])
        diccionario_datos["Condición del cielo"].append(datos[3])
        diccionario_datos["Visibilidad"].append(datos[4])
        diccionario_datos["Temperatura"].append(datos[5])
        diccionario_datos["Sensación térmica"].append(datos[6])
        diccionario_datos["Humedad"].append(datos[7])
        diccionario_datos["Viento"].append(datos[8])
        diccionario_datos["Presión"].append(datos[9])
    print(diccionario_datos)
        
    

        

    


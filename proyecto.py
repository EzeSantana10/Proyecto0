with open ("estado_tiempo20260910.txt", "r", encoding="cp1252") as archivo:

    datos = archivo.read()
    datos_limpios = datos.strip().split(";")

    datitos = {"ciudades/estación": datos_limpios[0], 
               "fecha": datos_limpios[1],
                "Hora": datos_limpios[2],
                "condicion_del_cielo" : datos_limpios[3]
    }
    print(datitos)
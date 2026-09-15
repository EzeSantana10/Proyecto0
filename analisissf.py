with open ("estado_tiempo20260910.txt", "r", encoding="cp1252") as archivo:

    datos = archivo.read()
    datos_limpios = datos.strip().split(";")

   print(datos_limpios)
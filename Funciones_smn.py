def measure_cities_read(diccionario) -> list:
    """
    ... La función toma la cantidad de ciudades en base a su posición como clave 
    ... y las manda a una lista. 
    """

    ciudades = []

    for clave, valor in diccionario:
        ciudades.append(clave)

    return ciudades

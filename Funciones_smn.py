from datetime import datetime

def leer_observaciones(archivo: str) -> dict:

    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""

    diccionario = {}

    with open (archivo, "r", encoding="cp1252") as file:

        for linea in file:
                linea_limpia = linea.strip()
                columnas = linea_limpia.split(";")
                ciudad = columnas[0]


                viento_sin_parsear = columnas[8].strip()
                direccion_viento, velocidad_viento = separar_viento(viento_sin_parsear)
                

                fecha = columnas[1].strip()
                hora = columnas[2].strip()
                fecha_y_hora = parsear_fecha_hora(fecha, hora)


                diccionario[ciudad] = {
                    "fecha y hora": fecha_y_hora,
                    "condicion": columnas[3].strip(),
                    "visibilidad": columnas[4].strip(),
                    "temperatura": columnas[5].strip(),
                    "sensacion_termica": columnas[6].strip(),
                    "humedad": columnas[7].strip(),
                    "direccion_viento": direccion_viento,
                    "velocidad_viento": velocidad_viento,
                    "presion": columnas[9].strip()
                }

    return diccionario



            
def parsear_fecha_hora(fecha: str, hora: str) -> datetime:

    """Convierte 'dd-mes-aaaa' y 'hh:mm' del SMN en un datetime."""
    
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio", 
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    
    fecha_formateada = fecha.lower()
    
    for i, mes in enumerate(meses, start=1):

        if mes in fecha_formateada:
            mes_num = f"{i:02d}"
            fecha_formateada = fecha_formateada.replace(mes, mes_num)
            break
            
    parseo = f"{fecha_formateada} {hora}"


    return datetime.strptime(parseo, "%d-%m-%Y %H:%M")




def separar_viento(campo_viento: str) -> tuple:

    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""

    componentes = campo_viento.split()
            
    if len(componentes) >= 2:
        direccion_viento = componentes[0]
            
        try:
            velocidad_viento = float(componentes[1])
        except ValueError:
            velocidad_viento = 0                            
    else:
        direccion_viento = campo_viento.strip() 
        velocidad_viento = 0

    return direccion_viento, velocidad_viento





def cantidad_ciudades(diccionario) -> list:
    """
    ... La función toma la cantidad de ciudades en base a su posición como clave 
    ... y las manda a una lista. 
    """

    ciudades = []

    for clave in diccionario:
        ciudades.append(clave)

    return f"La cantidad de ciudades leídas son un total de: {len(ciudades)} y estas son: {ciudades}"




def ciudades_completas(diccionario) -> list:
    """
    ... La función toma un diccionario y devuelve un entero donde el valor son
    ... la cantidad de ciudades completas (es decir las que no tienen None, ni "no se calcula").
    """

    ciudades_completas = 0
    lista_ciudades_completas = []

    for x, i in diccionario.items():

        if None not in i.values() and "No se calcula" not in i.values():
            ciudades_completas += 1
            lista_ciudades_completas.append(x)


    return f"La cantidad de ciudades completas es: {ciudades_completas} y estas son: {lista_ciudades_completas}"





def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:

    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
        (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
        como para viento."""
    
    lista_para_ordenar = []
    
    for ciudad, datos in observaciones.items():
        try:
            valor = float(datos[campo])
            lista_para_ordenar.append((ciudad, valor))
        except (ValueError, KeyError):
            continue
            
    lista_para_ordenar.sort(key=lambda x: x[1], reverse=descendente)
    
    return lista_para_ordenar[:n]
    



def horarios_reportados(observaciones: dict) -> list:

    """devuelve una lista de los horarios a los que las estaciones 
    reportaron en la observación dada. 
    La lista tendrá horas en el formato string "HH:MM",
    será sin repetir y ordenadas de menor a mayor"""

    lista = []

    for x, y in observaciones.items():
        solo_hora = y["fecha y hora"].strftime("%H:%M")
        if solo_hora not in lista:
            lista.append(solo_hora)

    lista_ordenada = sorted(lista)
    
    return lista_ordenada
    

def mostrar_resumen(observaciones: dict) -> None:

    """Imprime por pantalla el resumen con todas las características calculadas. Usar n=5"""

    print("--- RESUMEN DEL TIEMPO ---")
    print(f"Total de ciudades analizadas: {len(observaciones)}")
    print(cantidad_ciudades(observaciones))
    print(ciudades_completas(observaciones))
    print(f"Los horarios reportados son: {horarios_reportados(observaciones)}")
    print("Temperaturas más altas:")
    print(top_n_ciudades(observaciones, "temperatura", 5, True))
    print("Temperaturas más bajas:")
    print(top_n_ciudades(observaciones, "temperatura", 5, False))
    print("Mayor velocidad de viento:")
    print(top_n_ciudades(observaciones, "velocidad_viento", 5, True))
    
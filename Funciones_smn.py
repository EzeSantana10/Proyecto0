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

    return parseo



def cantidad_ciudades(diccionario) -> list:
    """
    ... La función toma la cantidad de ciudades en base a su posición como clave 
    ... y las manda a una lista. 
    """

    ciudades = []

    for clave in diccionario:
        ciudades.append(clave)

    return ciudades

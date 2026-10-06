from datetime import datetime

def convertir_dato(dato, es_num=False):

    if dato is None:
        return None
    
    dato = str(dato).strip()
    
    if dato in ("", "No se calcula", "-"):
        return None
        
    if es_num:
        try:
            dato_limpio = dato.replace(",", ".")
            num = float(dato_limpio)
            if num.is_integer():
                return int(num)
            else:
                return num
        except ValueError:
            return None
            
    return dato


def leer_observaciones(archivo: str, reporte: dict) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""

    reporte["lineas_invalidas"] = 0
    reporte["columnas_ausentes"] = 0
    reporte["faltantes_por_campo"] = {
        "condicion": 0,
        "visibilidad": 0,
        "temperatura": 0,
        "sensacion_termica": 0,
        "humedad": 0,
        "direccion_viento": 0,
        "velocidad_viento": 0,
        "presion": 0
    }

    diccionario = {}

    with open(archivo, "r", encoding="cp1252") as file:
        for linea in file:
            linea_limpia = linea.strip()
            columnas = linea_limpia.split(";")

            # Si faltan columnas, es una línea inválida/corta
            if len(columnas) < 10:
                reporte["columnas_ausentes"] += 1
                reporte["lineas_invalidas"] += 1
                continue

            try:
                ciudad = columnas[0].strip()
                viento_sin_parsear = columnas[8].strip()
                direccion_viento, velocidad_viento = separar_viento(viento_sin_parsear)

                fecha = columnas[1].strip()
                hora = columnas[2].strip()
                fecha_y_hora = parsear_fecha_hora(fecha, hora)

                datos_ciudad = {
                    "fecha y hora": fecha_y_hora,
                    "condicion": convertir_dato(columnas[3]),
                    "visibilidad": convertir_dato(columnas[4], es_num=True),
                    "temperatura": convertir_dato(columnas[5], es_num=True),
                    "sensacion_termica": convertir_dato(columnas[6], es_num=True),
                    "humedad": convertir_dato(columnas[7], es_num=True),
                    "direccion_viento": convertir_dato(direccion_viento),
                    "velocidad_viento": convertir_dato(velocidad_viento, es_num=True),
                    "presion": convertir_dato(columnas[9], es_num=True)
                }

                # Conteo de valores faltantes por campo
                for clave, valor in datos_ciudad.items():
                    if valor is None and clave in reporte["faltantes_por_campo"]:
                        reporte["faltantes_por_campo"][clave] += 1

                diccionario[ciudad] = datos_ciudad

            except Exception:
                reporte["lineas_invalidas"] += 1

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





def top_n_ciudades(observaciones: dict, campo: str, n: int = 5, descendente: bool = True, unidad: str = "") -> list:
    
    """Devuelve e imprime las ciudades ordenadas según 'campo' contemplando empates.
    Imprime el ranking de forma limpia y retorna la lista de tuplas (ciudad, valor)."""

    lista_datos = []

    for ciudad, info in observaciones.items():
        val = info.get(campo)
        
        if val is not None and isinstance(val, (int, float)):
            lista_datos.append([val, ciudad])

    lista_datos.sort(reverse=descendente)

    valores_top = []
    for item in lista_datos:
        valor = item[0]

        if valor not in valores_top:
            valores_top.append(valor)
        if len(valores_top) == n:
            break

    #Parte de impresión de datos:

    resultado = []
    puesto = 1
    val_anterior = None

    for i, item in enumerate(lista_datos, start=1):
        valor = item[0]
        ciudad = item[1]

        if valor in valores_top:
            resultado.append((ciudad, valor))

            if val_anterior is not None and valor != val_anterior:
                puesto = i
            val_anterior = valor

            print(f"  {puesto}. {ciudad}: {valor} {unidad}".strip())

    return resultado
    


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
    

def mostrar_resumen(observaciones: dict, lineas_invalidas: int = 0, columnas_ausentes: int = 0) -> None:
    """Imprime por pantalla el resumen con todas las características calculadas y el reporte de inconsistencias. Usar n=5"""

    print("--- RESUMEN DEL TIEMPO ---")
    print(f"Total de ciudades analizadas: {len(observaciones)}")
    print(cantidad_ciudades(observaciones))
    print(ciudades_completas(observaciones))
    print(f"Los horarios reportados son: {horarios_reportados(observaciones)}")

    print("\n--- LAS TOP N CIUDADES ---")
    print("Temperaturas más altas:")
    top_n_ciudades(observaciones, "temperatura", 5, True, "°C")
    print("Temperaturas más bajas:")
    top_n_ciudades(observaciones, "temperatura", 5, False, "°C")
    print("Mayor velocidad de viento:")
    top_n_ciudades(observaciones, "velocidad_viento", 5, True, "km/h")
    print("Menor velocidad de viento:")
    top_n_ciudades(observaciones, "velocidad_viento", 5, False, "km/h")

    print("\n--- REPORTE DE ARCHIVO ---")
    print(f"Líneas inválidas / omitidas: {lineas_invalidas}")
    print(f"Columnas ausentes: {columnas_ausentes}")
    
    
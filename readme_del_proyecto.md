# Análisis de Observaciones del SMN

Herramienta desarrollada en Python para procesar, validar y resumir datos meteorológicos a partir de los registros de observaciones del Servicio Meteorológico Nacional (SMN).

## 📥 Cómo conseguir el archivo de entrada

1. Ingresa a la página oficial de descarga de datos del **Servicio Meteorológico Nacional (SMN)**: [https://www.smn.gob.ar/descarga-de-datos] y descarga el archivo correspondiente al **estado del tiempo presente**.

2. Abre el archivo descargado. Dependiendo de tu configuración o sistema operativo, al abrirlo es posible que se descomprima automáticamente convirtiéndose en un archivo de texto plano (`.txt`), o bien que necesites extraerlo de forma manual utilizando un programa de descompresión.

3. Coloca el archivo `.txt` resultante en la misma carpeta del proyecto para que pueda ser utilizado y procesado correctamente.

## 🚀 Cómo ejecutar el proyecto y Ejemplo de Salida

Puedes ejecutar el script principal directamente desde la terminal pasando el archivo como argumento:

```
python analisis_smn.py archivo_observaciones.txt

```

Alternativamente, el proyecto utiliza un módulo de funciones (`Funciones_smn.py`) que puedes importar en tu script de la siguiente manera:

```
from Funciones_smn import mostrar_resumen

mostrar_resumen("archivo_observaciones.txt")

```

Al invocar la función, la salida por consola será la siguiente:

```
--- RESUMEN DEL TIEMPO ---
Total de ciudades analizadas: 121
La cantidad de ciudades leídas son un total de: 121 y estas son: ['Azul', 'Bahía Blanca', 'Benito Juárez', 'Bolívar', 'Campo de Mayo', 'Coronel Suarez', 'Dolores', 'El Palomar', 'Ezeiza', 'Junín', 'La Plata', 'Las Flores', 'Mar del Plata', 'Mariano Moreno', 'Merlo', 'Morón', 'Nueve de Julio', 'Olavarría', 'Pehuajó', 'Pigué', 'Punta Indio B.A.', 'San Fernando', 'Tandil', 'Trenque Lauquen', 'Tres Arroyos', 'Villa Gesell', 'Aeroparque Buenos Aires', 'Buenos Aires', 'Catamarca', 'Tinogasta', 'Pcia. Roque Saenz Peña', 'Resistencia', 'Comodoro Rivadavia', 'Esquel', 'Paso De Indios', 'Puerto Madryn', 'Trelew', 'Córdoba', 'Córdoba Observatorio', 'Esc. Aviación Militar', 'Laboulaye', 'Marcos Juárez', 'Pilar Obs.', 'Río Cuarto', 'Villa Dolores', 'Villa María Del Río Seco', 'Corrientes', 'Ituzaingó', 'Mercedes', 'Monte Caseros', 'Paso De Los Libres', 'Concordia', 'Gualeguaychú', 'Paraná', 'Formosa', 'Las Lomitas', 'Mount Pleasant Airport (Islas Malvinas)', 'La Quiaca', 'Jujuy', 'Jujuy Universidad Nacional', 'General Pico', 'Victorica', 'Santa Rosa', 'Chamical', 'Chepes', 'Chilecito', 'La Rioja', 'Malargue', 'Mendoza', 'Mendoza Observatorio', 'San Martín (Mza)', 'San Rafael', 'Uspallata', 'Bernardo De Irigoyen', 'Iguazú', 'Oberá', 'Posadas', 'Chapelco', 'Neuquén', 'Bariloche', 'Cipolletti', 'El Bolsón', 'Maquinchao', 'Río Colorado', 'San Antonio Oeste', 'Viedma', 'Metán', 'Orán', 'Rivadavia', 'Salta', 'Tartagal', 'Jachal', 'San Juan', 'San Luis', 'Santa Rosa del Conlara', 'Villa Reynolds', 'El Calafate', 'Gobernador Gregores', 'Perito Moreno', 'Puerto Deseado', 'Río Gallegos', 'San Julián', 'Santa Cruz', 'Ceres', 'Rafaela', 'Reconquista', 'Rosario', 'Santa Fe', 'Sunchales', 'Venado Tuerto', 'Termas de Rio Hondo', 'Santiago del Estero', 'Río Grande B.A.', 'Ushuaia', 'Tucumán', 'Base Belgrano II', 'Base Esperanza', 'Base Carlini', 'Base Marambio', 'Base Orcadas', 'Base San Martín']
La cantidad de ciudades completas es: 25 y estas son: ['Pcia. Roque Saenz Peña', 'Resistencia', 'Comodoro Rivadavia', 'Esquel', 'Paso De Indios', 'Las Lomitas', 'Mount Pleasant Airport (Islas Malvinas)', 'Chapelco', 'Bariloche', 'San Antonio Oeste', 'Orán', 'Rivadavia', 'Tartagal', 'El Calafate', 'Perito Moreno', 'Puerto Deseado', 'Río Gallegos', 'San Julián', 'Santa Cruz', 'Río Grande B.A.', 'Ushuaia', 'Base Belgrano II', 'Base Marambio', 'Base Orcadas', 'Base San Martín']
Los horarios reportados son: ['09:00', '10:00', '11:00', '12:00', '13:00', '15:00']
Temperaturas más altas: [('Rivadavia', 28.0), ('Orán', 27.4), ('Pcia. Roque Saenz Peña', 26.7), ('Tartagal', 26.4), ('Resistencia', 26.3)]
Temperaturas más bajas: [('Base Belgrano II', -28.6), ('Base San Martín', -24.8), ('Base Orcadas', -24.3), ('Base Marambio', -15.5), ('Base Esperanza', -9.5)]
Mayor velocidad de viento: [('Mount Pleasant Airport (Islas Malvinas)', 42.0), ('Perito Moreno', 38.0), ('Río Gallegos', 37.0), ('San Julián', 37.0), ('Comodoro Rivadavia', 33.0)]

```

## 🛠️ Funciones Individuales Disponibles

El módulo `Funciones_smn` encapsula la función principal de resumen, pero también permite utilizar de manera individual cada una de sus funciones internas según lo requieras:

* `leer_observaciones(archivo)`: Lee, parsea y valida el archivo de texto con las observaciones del SMN.

* `cantidad_ciudades(observaciones)`: Calcula y retorna el total junto con la lista completa de ciudades analizadas.

* `ciudades_completas(observaciones)`: Filtra y devuelve aquellas ciudades que cuentan con todos los registros completos.

* `horarios_reportados(observaciones)`: Extrae los diferentes horarios en los que se emitieron los reportes meteorológicos.

* `top_n_ciudades(observaciones, campo, n, descendente: bool = True)`: Función de ranking aplicable a variables numéricas (como temperatura o viento) para obtener las $N$ ciudades correspondientes:

  * **Parámetros**:

    * `observaciones`: Diccionario con la información procesada.

    * `campo`: El campo numérico a evaluar (por ejemplo, `"temperatura"` o `"viento"`).

    * `n`: Cantidad de ciudades a incluir en el ranking.

    * `descendente`: `True` para ordenar de mayor a menor (ej. temperaturas más altas / más viento) o `False` para ordenar de menor a mayor (ej. temperaturas más frías / menos viento).

  * **Casos de uso válidos**: Listado de las $N$ ciudades más cálidas, más frías, con más viento o con menos viento.
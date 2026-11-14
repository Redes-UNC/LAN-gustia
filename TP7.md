# Trabajo práctico N°  7 - Redes de Computadoras

**Grupo:** LAN-gustia

---

## Integrantes
* Alvarado, Jazmin
* Aroca Bustos, Nahuel Ezequiel
* Ibarra, Franco Ismael
* Lucero, Fabricio Agustin
* Soto, Milton Joaquin
* Zulaica, Federico Jose

---

## Desarrollo

## Parte 1: desafío 

* **IP, Máscara y Broadcast MAC**
A través del comando ipconfig, se obtuvo la dirección IPv4 **192.168.8.173** con máscara de subred **255.255.255.0**.

![alt text](img/ip.jpeg)

* **Procedimiento de Captura y Observaciones en Wireshark**

    * Configuración y Filtrado: Iniciamos la captura en Wireshark seleccionando el Wi-Fi correspondiente. Dado que la consigna indicaba que el mensaje se enviaba por difusión (broadcast) cada 30 segundos, aplicamos inmediatamente el filtro de visualización **eth.dst == ff:ff:ff:ff:ff:ff**. Esto nos permitió limpiar el ruido de la red del aula y aislar únicamente las tramas de Capa 2 dirigidas a todos los hosts.

    * Intercepción del Datagrama: Tras unos segundos de monitoreo, la lista de paquetes de Wireshark registró el ingreso de un datagrama dirigido a la dirección IP de broadcast de nuestra subred.

    * Inspección de la Carga Útil (Payload): Al hacer clic sobre el paquete interceptado, nos dirigimos al panel inferior de Wireshark (volcado hexadecimal y ASCII).

    * Extracción de Datos: Haciendo clic derecho sobre la sección de datos del paquete (Data), seleccionamos la opción Copy -> ...as Printable Text (o ASCII). Esto nos permitió llevar el contenido al portapapeles para su análisis.

* **Análisis Estructural del Mensaje**

El texto extraído de la carga útil de Wireshark reveló una estructura de datos estándar en formato JSON. El formato observado consta de los siguientes tres campos clave:

**"SIZE"**: Declara las dimensiones exactas de la matriz bidimensional original (indicando cantidad de Filas y Columnas).

**"PL" (Payload)**: Contiene una cadena continua de unos y ceros correspondientes al bloque de datos transmitido.

**"CHECK"**: Representa los bits de control calculados por el emisor (primero las paridades de las filas, luego las de las columnas).

* **Análisis y corrección del mensaje**

El mensaje recibido fue: 

{"SIZE": "8,7", "PL": "11010001110100111010011100001110011011101001011110101111111100111011111110101111010011101011100010110010101011101100011110111111011010101111111001111010001101111111001011101001110011010111111100010111000111011111001111001011111101010010101110111101000011000010100100011111111001101100101110000111101001110101111001010001010111101111001111010001100001111001011001010100000010000001000000100000", "CHECK": "011111010110111111110110011100101111001100001100110010001"}

detectamos fallas en 3 filas y 3 columnas, generando 6 permutaciones posibles. El texto extraído antes de aplicar las correcciones era: 
[https://youtube.com/shorts/q8wgKzJwPa$?featurE=share](https://youtube.com/shorts/q8wgKzJwPa$?featurE=share) 

el cual evidenciaba corrupción en tres caracteres (w, $, E).

* **Verificación de Integridad y Cálculo**
utilizamos el entorno de Python mediante el script **paridad.py** donde comparamos cada fila y columna con el correspondiente valor dado. 
El campo "SIZE" del payload dictaba las dimensiones: 8,7, lo que se traduce en una matriz de 8 filas por 49 columnas de bits (7 caracteres ASCII por fila x 7 bits por carácter).Al reconstruir la matriz de datos con los bits del campo "PL" y recalcular la paridad par de cada eje, cruzamos nuestros resultados con los bits originales de control del el campo "CHECK". El análisis detectó discrepancias que fueron las siguientes: 

    Fila 4, Fila 5 y Fila 6.Columnas con falla de paridad: Columna 8, Columna 16 y Columna 22.
    
* **Ubicación y Corrección de Errores Múltiples**
Una vez resuelta la matriz (invirtiendo los bits) se utilizó el script **decodificar_mensaje.py**, con el que se obtuvo el siguiente enlace:
:[https://youtube.com/shorts/q8WgKzJwPa4?feature=share](https://youtube.com/shorts/q8WgKzJwPa4?feature=share)


## Parte 2: consignas teóricas 

### 1. ¿Que huebiera pasado si el mensaje tenia errores en dos bits de filas y columnas distintas?¿Y si se dañaba un bit de los de control?
 Para dos errores en filas y columnas distintas.Fallan 2 filas y 2 columnas, que se cruzan en 4 posiciones.El error se detecta pero no se puede corregir, y hay que pedir que se reenvíe el mensaje.

Un bit de control dañado. Falla una sola fila o una sola columna, nunca las dos a la vez. Un error en los datos siempre hace fallar las dos, así que esto indica que el bit dañado es el de control. Los datos están bien y no hay que corregir nada.
 

### 2. Si el mensaje es texto en castellano, muchas veces un error "se adivina" por contexto (Hola mondo). ¿Sirve eso para una contraseña, un número de cuenta o una dirección web? ¿Qué aporta el código frente a "leer y adivinar"? 
No sirve: si una palabra no existe, el lector se da cuenta; una contraseña, un número de cuenta o una URL no tienen esa redundancia. Si cambia un carácter, el resultado sigue siendo válido: no hay forma de notar el error ni de saber cuál era el valor original. Además, en ASCII invertir un solo bit casi siempre da otro carácter válido, así que un mensaje puede “leerse bien” y estar mal.

El código agrega una redundancia pensada para esto, que no depende del significado del mensaje. Detecta el error con cualquier tipo de dato, indica la fila y la columna del bit equivocado y permite corregirlo sin pedir que se reenvíe el mensaje.

### 3. 

### 4. 
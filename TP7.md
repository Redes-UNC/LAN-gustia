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

## Parte 2: consignas teóricas 

### 1. ¿Que huebiera pasado si el mensaje tenia errores en dos bits de filas y columnas distintas?¿Y si se dañaba un bit de los de control?
 Para dos errores en filas y columnas distintas.Fallan 2 filas y 2 columnas, que se cruzan en 4 posiciones.El error se detecta pero no se puede corregir, y hay que pedir que se reenvíe el mensaje.

Un bit de control dañado. Falla una sola fila o una sola columna, nunca las dos a la vez. Un error en los datos siempre hace fallar las dos, así que esto indica que el bit dañado es el de control. Los datos están bien y no hay que corregir nada.
 

### 2. Si el mensaje es texto en castellano, muchas veces un error "se adivina" por contexto (Hola mondo). ¿Sirve eso para una contraseña, un número de cuenta o una dirección web? ¿Qué aporta el código frente a "leer y adivinar"? 
No sirve: si una palabra no existe, el lector se da cuenta; una contraseña, un número de cuenta o una URL no tienen esa redundancia. Si cambia un carácter, el resultado sigue siendo válido: no hay forma de notar el error ni de saber cuál era el valor original. Además, en ASCII invertir un solo bit casi siempre da otro carácter válido, así que un mensaje puede “leerse bien” y estar mal.

El código agrega una redundancia pensada para esto, que no depende del significado del mensaje. Detecta el error con cualquier tipo de dato, indica la fila y la columna del bit equivocado y permite corregirlo sin pedir que se reenvíe el mensaje.

### 3. 

### 4. 
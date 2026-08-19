# Trabajo práctico N° 2 - Redes de Computadoras

**Grupo:** LAN-gustia

---

## Integrantes
*
*
*
*
*
*

---

## Desarrollo

# 1. 

# 2. 

# 3. 

# 4. Interpretacion de la informacion y tramas

## 4.a. Sincronizacion en comunicacion digitales

En una comunicacion digital, la sincronizacion es el proceso mediante el cual el receptor logra coordinarse temporalmente con el transmisor para poder interpretar correctamente la señal recibida. Esto es necesario ya que los datos se transmiten como una secuencia de bits, y el receptor debe determinar cuando se debe realizar cada lectura y como agrupar los bits.

### Sincronizacion de bits

La sincronizacion de bits consiste en determinar los intantes de tiempo en los cuales se debe realizar la lectura de la señal recibida para poder interpretar correctamente cada uno de estos bits. Si esto no se realiza correctamente se pueden perder bits, interpretar erroneamente o tener lecturas duplicadas.

### Sincronizacion de trama

Luego identificar correctamente los bits individuales, el receptor necesita determinar que bits pertenecen a cada trama. Para esto es necesario poder identificar donde comienza y donde termina cada una de ellas. Para hacerlo se aplican diferentes tecnicas, como secuencias especiales, campos de longitus o estructura de tamaño conocido.

## 4.b. Tramas y sus componentes

Una trama es una unidad de datos que se utiliza en comunicacion. Aparte de contener la informacion a trasmitir, normalmente tambien lleva informacion adicional necesaria para controlar, identificar y verificar la transmision.

### Header:

Aparece al comienzo de la trama, contiene informacion de control necesaria para interpretar o procesar la trama. Por ejemplo, direcciones, informacion de control, identificadores, etc.

### Payload:

Es la informacion que realmente se quiere transmitir.

### Trailer:

Aparece al final de la trama y contiene informacion adicional necesaria para el control y la verificacion de la transmision. Por ejemplo, informacion de control de errores, etc.

# 5.

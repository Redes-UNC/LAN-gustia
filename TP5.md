# Trabajo práctico N°  5 - Redes de Computadoras

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







 # 3 TCP y UDP "a mano" con ncat

## 3A
Establecer una conexión significa que dos procesos se pongan de acuerdo antes de intercambiar datos, sincronizando sus números de secuencia iniciales y otros parámetros. Esto se realiza mediante los paquetes de sincronizacion y confirmación. Una conexion existe unicamente en los extremos, al establecerse cada entidad de transporte reserva recursos y lleva la cuenta de los segmentos enviados y recibidos. Los cables y los routers no guardan informacion de la conexion 

## 3B
Un puerto es un numero que identifica a un proceso o aplicacion dentro de un host, este es unico dentro del host otro host puede usar el mismo puerto para otro proceso por eso el par IP/puerto es el que identifica el extremo de la comunicacion

## 3C
Que un proceso esté escuchando en un puerto significa que le pidió al sistema operativo que le entregue las solicitudes de conexión o los datos que lleguen a ese puerto.

## 3A
![alt text](img/ConexionTcp.png)


![alt text](img/ConexionUDP.png)

Se puede observar que no realiza un handshake previo y en UDP el cliente solo registra la direccion (IP/puerto). En TCP, al ejecutar el cliente si realizo el handshake antes de enviar cualquier dato

## 3B
En UDP cada mensaje genero un datagrama sin ACK, el receptor no confirma la recepción, mientras que TCP usa 2 segmentos el primero que es el que lleva los datos y el segundo que confirma la recepcion de los mismos

## 3C

![alt text](img/WireSharkTcp.png)

![alt text](img/WiresharkUDP.png)

Ambos encabezados tienen puerto origen, puerto destino y checksum. El de UDP agrega solo la longitud, y ocupa 8 bytes en total. El de TCP ocupa 20 bytes y ademas tiene: número de secuencia, número de ACK, longitud del encabezado, flags, ventana y puntero urgente

## 3D

![alt text](img/CierreConexionTCP.png)

![alt text](img/CierreConexionUDP.png)

Al cerrar el cliente TCP con Ctrl+C se generaron 4 segmentos: un FIN desde cada extremo, cada uno confirmado con su ACK, y el servidor terminó al recibir el FIN del cliente. En cambio, en UDP no se envió ningún paquete, ya que no existe una conexión que cerrar, y el servidor nunca se enteró de que el cliente había terminado.

## 3E

![alt text](img/CantPaquetes.png)

![alt text](img/CantPaquetesUdp.png)

En TCP se necesitaron 9 paquetes mientras que en UDP se necesito solo 1. Con los paquetes extra compramos confiabilidad y tranquilidad de que funcionó correctamente la transmisión de los datos

## 3F

![alt text](img/Cmd.png)


![alt text](img/WiresharkConexionre.png)

Al intentar conectarse por TCP a un puerto sin ningún proceso escuchando, el cliente mandó un SYN y el sistema respondió con un segmento RST-ACK, rechazando la conexión. Se intentó 4 veces más con el mismo resultado. En UDP, el cliente indicó que estaba conectado aunque nadie escuchaba; al enviar el datagrama, el sistema respondió con un Destino inalcanzable (Puerto inalcanzable).

## 4.A a 4.C

Inicialmente, se replicó el proceso detallado en las intrucciones del tp. Usando los scripts de python *tcp_server.py* y *tcp_client.py*, y wireshark, filtrando con *tcp.port == 12000* tendremos los siguientes resultados: 
- Ejecutando **tcp_server**

![alt text](img/4.a_1.png)

- y posteriormente **tcp_client** (en este caso el mensaje quedó por defecto)

![alt text](img/4.a_2.png)

![alt text](img/4.a_3.png)

Luego, podremos ver mediante el filtrado antes mencionado que: 

![alt text](img/4.a.png)

1. **Connect(): establecimiento de la conexión** 

![alt text](img/4.d.png)

*    a. El cliente envía un segmento con el flag [SYN].
*    b. El servidor responde con [SYN, ACK].
*    c. El cliente confirma con un [ACK].

2. **Sendall(): Transferencia de datos**

A continuación podremos ver los paquetes que contienen los mensajes reales. 

![alt text](img/4.d_1.png)

* a. Un paquete del cliente al servidor con los flags [PSH, ACK]. Acá se ve el texto "Hola servidor".

![alt text](img/4.d_2.png)

* b. Un [ACK] de respuesta del servidor (invisible en el código, lo manda el sistema operativo).

![alt text](img/4.d_3.png)

* c. Otro paquete [PSH, ACK] del servidor al cliente con la respuesta ("Recibido: Hola servidor...")

![alt text](img/4.d_4.png)

3. **Close(): cierre de la conexión**

y por último, para el proceso de cierre observamos los siguientes: 

![alt text](img/4.d_5.png)

* a. Un segmento con el flag [FIN, ACK] del cliente hacia el servidor.
* b. El servidor responde con un [ACK] y luego envía su propio [FIN, ACK].
* c. El cliente envía el [ACK] final.

## 4.D 

Con lo observado en los incisos anteriores podemos dar la siguiente información: 

| Llamada | ¿Donde se ejecuta? | ¿genera tráfico? | Segmentos que observan |
| :--- | :---: | ---: | ---: |
| socket() | Servidor y cliente | No | Ninguno. |
| bind() | servidor | No | Ninguno. |
| listen() | servidor | No | Ninguno. |
| connect() | cliente | Si | Paquetes 32, 33 y 34. Se observa el Three-way handshake inicial con la secuencia de flags [SYN] en el paquete 32, [SYN, ACK] en el 33, y la confirmación [ACK] en el 34.  |
| accept() | servidor | No | Ninguno. |
| sendall() | servidor | Si | Paquetes 35, 36, 37. Se observan los segmentos con el flag [PSH, ACK] que transportan los datos. "Hola servidor" en el paquete 35, la respuesta "Recibido: Hola servidor" en el paquete 37,  y  Un [ACK] de respuesta del servidor en el 36|
| recv() | servidor | No | Ninguno. |
| close() | ambos | Si | Paquetes 39, 40, 41 y 42. Se observa el proceso de cierre ordenado con los segmentos que llevan el flag [FIN, ACK] enviados por ambos extremos (paquetes 39 y 41), intercalados con sus respectivas confirmaciones [ACK] (paquetes 40 y 42). |
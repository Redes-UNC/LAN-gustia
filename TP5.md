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
# Trabajo práctico N° 2 - Redes de Computadoras

**Grupo:** LAN-gustia

---

## Integrantes
* Alvarado, Jazmin
* Aroca Bustos, Nahuel Ezequiel
* Ibarra, Franco Ismael
* Lucero, Fabricio Agustin
* Soto, Milton Joaquin
* Zulaica, Federico

---

## Desarrollo

# 1. 
![alt text](<img/figura p1.png>)

## 1.a 
El fenómeno que se está representando en el gráfico es el "Efecto Doppler", esto lo podemos saber gracias a que si observamos la onda en el dibujo, notamos que cerca del barco los picos están más separados (mayor longitud de onda), pero a medida que se acercan al satélite, los picos se "aprietan" o comprimen (menor longitud de onda).

## 1.b 
Las bandas más afectadas por el efecto doppler son Las bandas de alta frecuencia (como **SHF o EHF**, usadas justamente para enlaces satelitales) sufren el impacto más severo. El desfasaje o error de frecuencia ($\Delta f$) que sufre la señal se calcula multiplicando la frecuencia original ($f_0$) por la velocidad relativa entre los equipos ($v$) dividida la velocidad de propagación ($c$):

$$\Delta f = f_0 \left( \frac{v}{c} \right)$$

Como la frecuencia original ($f_0$) está multiplicando de forma directa, el error crece proporcionalmente.

- Si un auto se mueve transmitiendo en una banda de baja frecuencia (ej. radio FM a $100 \text{ MHz}$), el $\Delta f$ es de apenas unos pocos hercios. El receptor ni se entera.
- Si un satélite se mueve transmitiendo a $15 \text{ GHz}$ (alta frecuencia), el multiplicador es enorme. El corrimiento puede ser de decenas de miles de hercios. La señal se sale totalmente del canal esperado, y si el receptor intenta leer esa onda escalonada (como la que graficaron en el TP1) en los tiempos equivocados, va a decodificar ruido y basura en lugar de unos y ceros.

Las más resilientes son las transmisiones en bajas frecuencias (**VHF o la parte baja de UHF**). Son inherentemente inmunes a grandes estragos porque sus longitudes de onda son inmensas (metros o kilómetros). El desfase que sufren es numéricamente despreciable para la mayoría de las aplicaciones terrestres.

## 1.c 
La prohibición de usar celulares en vuelo se originó por precaución ante posibles interferencias con los instrumentos de navegación. Sin embargo, desde el punto de vista de las telecomunicaciones terrestres, el Efecto Doppler y la altitud son el gran problema:

- **Velocidad extrema:** Un avión comercial viaja a unos 900 km/h. A esa velocidad, el Efecto Doppler de la onda electromagnética que el celular envía hacia la antena en tierra es muy alto. Las redes celulares convencionales están diseñadas para tolerar y corregir el Doppler que genera un auto moviéndose por la autopista, no un avión.

- **Línea de visión:** Al volar a miles de metros de altura, no hay edificios ni montañas. Tu celular de repente tiene línea de visión directa con decenas o cientos de celdas celulares en distintas ciudades al mismo tiempo.

- **Saturación:** Sumando el rápido cambio de frecuencia por el Doppler y la altitud, el teléfono, al no entender bien la geometría de la red, transmite a máxima potencia intentando conectarse y registrarse en todas las torres a la vez. Esto genera un "ping-pong" que satura los recursos y el enrutamiento de la red móvil en tierra.


# 2. 
![alt text](<img/FiguraP2.png>)

## 2.a
El fenómeno físico que se está representando se denomina “Ruido impulsivo”.

Este fenómeno es discontinuo y está constituido por pulsos o picos de corta duración con una amplitud relativamente alta. Es provocado por eventos electromecánicos o transitorios bruscos (en la figura, las chispas y arrastres del motor de la herramienta del operario). Constituye una de las principales causas de error en la comunicación digital de datos, ya que un solo pico de alta energía altera un bloque entero de bits;  en cambio, en la transmisión analógica solo genera una pequeña degradación o chasquido imperceptible sin mayor trascendencia.

## 2.b
Este fenómeno afecta más a las transmisiones de bandas bajas y medias de la ITU (ELF a HF/VHF, por convivir con maquinaria cerca del suelo), sistemas de banda angosta (el pulso concentra más energía dentro del canal) y cables de cobre sin blindaje.

Las transmisiones más resilientes son las de bandas altas de la ITU (SHF/EHF, con enlaces directivos y alejados del suelo), sistemas de banda ancha (el impacto se diluye en el ancho de banda), medios apantallados y la fibra óptica (totalmente inmune por transmitir luz).

## 2.c
La SNR (Signal-to-Noise Ratio) se define como el cociente de la potencia de la señal entre la potencia del ruido presente en un punto determinado en el medio de transmisión. Generalmente, este cociente se mide en el receptor, ya que es aquí donde se realiza el procesado de la señal y la eliminación del ruido no deseado. Por cuestiones de comodidad,la SNR se expresa en decibelios(dB):

$$SNR_{dB} = 10 \log_{10} \frac{\text{potencia de señal}}{\text{potencia de ruido}}$$

La SNR está relacionado directamente con el BER (Bit Error Rate), que es la proporción de bits erróneos recibidos respecto al total de bits transmitidos en un canal digital. El vínculo entre ambos es inversamente proporcional: una alta SNR le permite al receptor diferenciar la información del ruido, reduciendo la tasa de errores (menor BER). En cambio, cuando la SNR cae por un incremento en el ruido, el receptor confunde los estados de la señal y la probabilidad de alterar un bit aumenta, elevando consecuentemente el BER. 


# 3.

**Sobre el ruido en el canal:** Los sistemas digitales ayudan agregando bits de redundancia a la transmisión. Gracias a estos códigos, el receptor puede identificar si la señal llegó con errores debido al ruido y corregirlos por su cuenta, sin necesidad de pedir una retransmisión.

**Sobre los cambios en la frecuencia:** Para compensar esto, el receptor utiliza técnicas de procesamiento para sincronizarse con la señal. Va estimando las variaciones de frecuencia del canal y ajusta su referencia, utilizando recuperación de portadora y ecualización, para recuperar los símbolos sin perder la información.

Por lo tanto, la redundancia ayuda frente al ruido, mientras que la sincronización y el procesamiento de la señal sirven contra las variaciones de frecuencia.

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

## 4.c.
El preámbulo es una secuencia de bits que se coloca antes de una trama y que permite al receptor prepararse para recibirla. Entre sus funciones se encuentran la sincronización entre el transmisor y el receptor y la identificación del comienzo de una trama.
No necesariamente forma parte de la información que se desea transmitir. Generalmente se utiliza como información de control, necesaria para que el receptor pueda detectar y procesar correctamente la trama antes de recibir los datos propiamente dichos.

## 4.d. 
El protocolo puede determinar dónde termina una trama mediante:

* Longitud fija: Todas las tramas tienen un tamaño previamente establecido. El receptor sabe de antemano cuántos bits o bytes debe recibir para completar una trama.

* Campo de longitud: La trama contiene un campo dentro de su encabezado que indica su longitud. El receptor lee este valor y sabe cuántos bytes pertenecen a la trama.

* Secuencia delimitadora: Se utiliza una secuencia especial de bits o caracteres para indicar el comienzo o el final de una trama. Cuando el receptor encuentra dicha secuencia, interpreta que la trama ha finalizado.

# 5.

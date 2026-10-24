# Trabajo práctico N°  6 - Redes de Computadoras

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

# Parte 1: Taller de armado y verificación de cables Cat5/Cat5e bajo estándar T568A/B.





# Parte 2: Equipamiento físico, verificación y utilización de equipos de red y generación de tráfico.

## Levantar y testear una LAN
## 1) 

Para realizar la actividad, se configuró manualmente la interfaz de red de una computadora, asignándole una dirección IPv4, una máscara de subred y una puerta de enlace predeterminada.

Los valores de ejemplo utilizados para documentar la configuración son:

| Parámetro | Valor |
|---|---|
| Dirección IPv4 | `192.168.1.10` |
| Máscara de subred | `255.255.255.0` |
| Puerta de enlace predeterminada | Sin configurar |

<img width="1033" height="697" alt="IP FIJA" src="https://github.com/user-attachments/assets/1f74c362-bc32-4045-88db-4f0d15980206" />

### d) Justificación de las direcciones elegidas

La dirección IPv4 identifica la interfaz de red de la computadora dentro de la LAN. Se eligió una dirección privada perteneciente al rango `192.168.1.0/24`, utilizado habitualmente en redes locales.

La máscara `255.255.255.0` equivale a `/24`. Esto permite que las computadoras con direcciones pertenecientes a la misma subred se comuniquen directamente a través del switch, sin necesidad de que un router intervenga en la comunicación local.

Para que la comunicación funcione, cada computadora debe tener una dirección IP única dentro de la subred y una máscara compatible con la del resto de los equipos.

La puerta de enlace predeterminada se utiliza para enviar paquetes hacia redes diferentes de la red local. Si la actividad se realiza únicamente entre computadoras conectadas al mismo switch, sin un router, no es necesaria para comunicarse entre ellas. Por lo tanto, no corresponde asignar una dirección de gateway ficticia.

## 2) 

Una vez configuradas las interfaces de red, se conectó una computadora por grupo al switch TP-LINK mediante los cables armados

### Verificación de conectividad mediante ping

Se utilizó  `ping` para comprobar la comunicación entre computadoras de distintos grupos, enviando solicitudes ICMP Echo Request a la dirección IPv4 de la otra computadora.
Nuestra computadora tenia la ip `192.168.1.10` y la otra la `192.168.1.11`

|Ping a `192.168.1.10` | 
| <img width="904" height="286" alt="ping a 1 11" src="https://github.com/user-attachments/assets/66c93acc-0f1f-46e8-a18c-cf5a7a303e23" />|

|Ping a `192.168.1.11` | 
| <img width="1600" height="843" alt="ping a 1 10" src="https://github.com/user-attachments/assets/ee5a3b9c-352e-472c-8c54-0488b613eb7a" />|

Al recibir respuestas, se confirma que existe conectividad IP entre las dos computadoras en ese momento.

## Desarrollar un pequeño servidor



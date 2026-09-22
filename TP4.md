# Trabajo práctico N° 4 - Redes de Computadoras

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

# 1. 


# 2.
 La red consiste en dos computadoras (PC-A y PC-B) conectadas a través de dos switches (SW-1 y SW-2).

 * **Conexiones de Datos:** Se utilizan cables directos (FastEthernet) entre las PCs y los switches, y un cable cruzado entre los dos switches.

 * **Conexiones de Administración:** Se configuran cables de consola (RS-232 a Console) desde cada PC a su respectivo switch para su gestión inicial.

 ![Topologia](./img/2.Topologia.png) 

## Tabla de Direccionamiento

 | **Device** | **Interface** | **IP Address** | **Subnet Mask** | **Default Gateway** |
 | ---------- | ------------- | -------------- | --------------- | ------------------- |
 | **SW-1**   | VLAN 1        | 192.168.1.11   | 255.255.255.0   | N/A                 |
 | **SW-2**   | VLAN 1        | 192.168.1.12   | 255.255.255.0   | N/A                 |
 | **PC-A**   | NIC           | 192.168.10.3   | 255.255.255.0   | 192.168.10.1        |
 | **PC-B**   | NIC           | 192.168.10.4   | 255.255.255.0   | 192.168.10.1        |

 Se configuraron las direcciones IP estáticas desde la interfaz gráfica de las computadoras (Desktop > IP Configuration).

 | IP PC-A | IP PC-B |
 | :---: | :---: |
 | ![Ruteo](./img/2.ruteoPC-A.png) |![Ruteo](./img/2.ruteoPC-B.png) |

## 2.a
 Desde la terminal de las PCs (vía cable de consola), se ingresó al modo de configuración global para designar los nombres correspondientes (SW-1 y SW-2).
 | Designación del nombre de sw2 (mismo precedimiento para sw1)| 
 | :---: |
 |![Nombre](./img/2.a.name.sw2.png) |

## 2.b y 2.c

 Para proteger el acceso a los dispositivos, se configuraron contraseñas para el modo privilegiado (*class*), el acceso por consola (*cisco*) y el acceso remoto VTY (*cisco*).

 - *(config)# enable secret class*

 - *(config-line)# password cisco*

 - *(config)# line vty 0 15*

 - *(config-line)# password cisco*

 Para evitar que las contraseñas de consola y VTY se lean en texto plano en la configuración del equipo, se habilitó el servicio de encriptación.

 - *(config)# service password-encryption*
 
 | Asignación y encriptación sw1 | Asignación y encriptación sw2 |
 | :---: | :---: |
 |![ContraseñasPC-A](./img/2.b.c.passwordPC-A.png) | ![ContraseñasPC-B](./img/2.b.c.passwordPC-B.png) |

## 2.d
 Se asignaron las direcciones IP de administración a la VLAN 1 de ambos switches, colocando las interfaces correspondientes.
 | Red VLAN sw1 | Red VLAN sw2 |
 | :---: | :---: |
 | ![ConfigVLAN-sw1](./img/2.d.VLAN.sw1.png) | ![ConfigVLAN-sw2](./img/2.d.VLAN.sw2.png) |

 

## 2.e
Se utilizó el comando show ip interface brief para identificar las interfaces utilizadas y las que se encontraban libres. En ambos switches, Fa0/1 y Fa0/2 son las interfaces utilizadas en la topología. Las demás interfaces fueron deshabilitadas mediante el comando shutdown

| sw1 |  sw2 |
 | :---: | :---: |
 |<img width="723" height="712" alt="image" src="https://github.com/user-attachments/assets/0fbe89f1-e327-4f17-84da-28dcd30c866a" /> | <img width="828" height="714" alt="image" src="https://github.com/user-attachments/assets/36564a10-f087-44a9-b7f1-fdf0da8cc1e3" /> |



## 2.f
Una vez finalizada la configuración de los switches, se guardó la configuración realizada para evitar que los cambios se pierdan al reiniciar los dispositivos.

En SW1 y SW2 se utilizó write memory


|<img width="662" height="120" alt="image" src="https://github.com/user-attachments/assets/cf326285-38e3-4dd9-9554-d5f0c236e7ca" />|


## 2.g
Se verificó la comunicación entre los dispositivos mediante el comando ping.


 | ping desde PC-A hacia PC-B | ping desde PC-B hacia PC-A|
 | :---: | :---: |
 | <img width="850" height="364" alt="image" src="https://github.com/user-attachments/assets/3f19496d-48b0-4ddb-92e2-5613fd7ef5ae" /> |<img width="796" height="414" alt="image" src="https://github.com/user-attachments/assets/8fe0a2cc-8622-4dab-88da-19a3495d6787" /> |

## 2.h
Se creo las siguientes VLANs en ambos switches. 
VLAN 10: Laboratorio
VLAN 20: Bar
VLAN 99: Management
verificando la configuración mediante show vlan brief


| sw1 |  sw2 |
 | :---: | :---: |
 |<img width="721" height="592" alt="image" src="https://github.com/user-attachments/assets/cc612d5a-ee5a-432c-a185-9277a8bec32b" /> | <img width="713" height="482" alt="image" src="https://github.com/user-attachments/assets/4c46d14a-6ee9-4d54-8657-c4bc48f2a120" /> |


## 2.i

## 2.j

## 2.k

## 2.l

## 2.m

## 2.n

# 3. Simulacion de Red LAN a bordo

**1. Topologia de Red**

![Nombre](./img/topologia.png)

**2. Configuracion Logica**
Se segmento la red en tres areas con distintos privilegios:
* **VLAN10 (Turista - 10.10.10.0/24):** Se aplico un ACL (LIsta de Control de Acceso) para denegar el trafico externo, limitando la conexion solo al servidor local.
* **VLAN20 (Business - 10.10.20.0/24):** Se configuro NAT dinamico para permitir la salida a Internet y acceso al servidor.
* **VLAN99 (Admin - 10.10.99.0/24):** Cuenta con enrutamiento y acceso total a cualquier destino.

**3. Pruebas**

*   **Turista:** Ping exitoso y HTTP web a `10.10.99.10`. Ping a `8.8.8.8` denegado (Destination host unreachable).

![Nombre](./img/Turista1.png)
![Nombre](./img/Turista2.png)

*   **Business:** HTTP web a `10.10.99.10` funcional y ping exitoso a `8.8.8.8`.

![Nombre](./img/Business2.png)
![Nombre](./img/Business1.png)

*   **Admin:** Pings exitosos a todos los dispositivos (servidor, Internet y PCs).

![Nombre](./img/Admin.png)

**4. Conclusión**
El uso de **VLANs** permitió aislar el tráfico de los pasajeros en una misma infraestructura. Al combinar esto con NAT para la salida a Internet y ACLs para filtrar paquetes, se logró aplicar con éxito la política comercial de la aerolínea: dar internet a Business y restringir a Turista exclusivamente al entretenimiento a bordo.

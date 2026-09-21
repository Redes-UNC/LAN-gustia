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

## 2.f

## 2.g

## 2.h

## 2.i

## 2.j

## 2.k

## 2.l

## 2.m

## 2.n

# 3.

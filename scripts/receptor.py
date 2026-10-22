import socket

# Configuración
HOST = "0.0.0.0"  # 0.0.0.0 permite escuchar en todas las interfaces de red (Wi-Fi, Ethernet, etc.)
PORT = 5000       # Puerto especificado en el TP6

# 1. Crear el socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Asociar el socket a la IP y puerto
servidor.bind((HOST, PORT))

print(f"[RECEPTOR] Escuchando tráfico UDP en el puerto {PORT}...")

try:
    while True:
        # 3. Recibir datos (hasta 1024 bytes por paquete)
        datos, direccion_cliente = servidor.recvfrom(1024)
        
        # 4. Decodificar e imprimir el mensaje
        mensaje = datos.decode('utf-8', errors='replace')
        print(f"Recibido de {direccion_cliente[0]}:{direccion_cliente[1]} -> {mensaje}")
except KeyboardInterrupt:
    print("\n[RECEPTOR] Servidor apagado.")
    servidor.close()
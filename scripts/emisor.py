import socket

# Configuración
IP_DESTINO = "192.168.1.10"  # Reemplaza esto con la IP de la computadora que corre el Receptor
PORT = 5000

# 1. Crear el socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[EMISOR] Listo para enviar datagramas a {IP_DESTINO}:{PORT}")
print("Escribe un mensaje y presiona Enter (o escribe 'salir' para terminar).")

while True:
    mensaje = input("> ")
    
    if mensaje.lower() == 'salir':
        break
        
    # 2. Enviar el mensaje codificado en bytes a la IP y puerto destino
    cliente.sendto(mensaje.encode('utf-8'), (IP_DESTINO, PORT))

cliente.close()
print("[EMISOR] Cliente cerrado.")
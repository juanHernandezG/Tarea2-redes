import socket

# Función para manejar la conexión de cada cliente
def handle_client(client_socket, client_address):
    print(f"Cliente conectado desde {client_address}")

    # Recibe el nombre del estudiante
    student_name = client_socket.recv(1024).decode()
    print(f"Nombre del estudiante: {student_name}")

    while True:
        # Recibe el mensaje del cliente
        message = client_socket.recv(1024).decode()

        # Comprueba si el cliente quiere desconectar
        if message.lower() == "desconectar":
            break

        print(f"Mensaje recibido del cliente: {message}")

        # Retransmite el mensaje al cliente
        client_socket.send(message.encode())

    print(f"Cliente {student_name} desconectado.")
    client_socket.close()

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("'127.0.0.1'", 8080)
server_socket.bind(server_address)
server_socket.listen(5)
print("Servidor en espera de conexiones...")

while True:
    # Espera la conexión de un cliente
    client_socket, client_address = server_socket.accept()

    # Inicia un nuevo hilo para manejar la conexión del cliente
    handle_client(client_socket, client_address)

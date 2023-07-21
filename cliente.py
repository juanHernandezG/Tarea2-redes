import socket

# Configuración del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12345)

try:
    # Establece la conexión con el servidor
    client_socket.connect(server_address)
    print("Conexión establecida con el servidor.")

    # Envía el nombre del estudiante
    student_name = input("Ingrese su nombre: ")
    client_socket.send(student_name.encode())

    while True:
        # Envía un mensaje al servidor
        message = input("Ingrese un mensaje ('desconectar' para salir): ")
        client_socket.send(message.encode())

        # Comprueba si el cliente quiere desconectar
        if message.lower() == "desconectar":
            break

        # Recibe la respuesta del servidor
        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")

except ConnectionRefusedError:
    print("No se puede establecer una conexión con el servidor.")

finally:
    client_socket.close()

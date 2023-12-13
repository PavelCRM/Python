import socket
import threading

clients = {}  # Словарь для хранения соединений и ников клиентов


def handle_client(client_socket, addr):
    global clients
    nickname = client_socket.recv(1024).decode()
    clients[client_socket] = nickname
    print(f"Подключен клиент: {nickname}")

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break

            message_str = message.decode()
            # Если сообщение начинается с '@', это личное сообщение
            if message_str.startswith("@"):
                recipient, _, msg = message_str.partition(" ")
                recipient = recipient[1:]  # Убираем '@' из ника получателя
                found = False
                for c, nick in clients.items():
                    if nick == recipient:
                        c.sendall(f"Личное от {nickname}: {msg}".encode())
                        found = True
                        break
                if not found:
                    client_socket.sendall(
                        f"Клиент с ником '{recipient}' не найден.".encode()
                    )
            else:
                for c in clients:
                    if c != client_socket:
                        c.sendall(f"{nickname}: {message}".encode())
    except ConnectionResetError:
        print(f"Клиент {nickname} отключился.")
    finally:
        client_socket.close()
        del clients[client_socket]


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 5555)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Сервер запущен на адресе:", server_address)

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, client_address)
        )
        client_handler.start()


start_server()

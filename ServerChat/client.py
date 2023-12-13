import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            decoded_message = message.decode()
            if decoded_message.startswith("[SERVER]"):
                print(decoded_message)
            else:
                print("Получено от сервера:", decoded_message)
        except ConnectionResetError:
            print("Сервер отключен.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5555)

    try:
        client_socket.connect(server_address)
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        nickname = input("Введите ваш ник: ")
        client_socket.sendall(nickname.encode())

        while True:
            message = input("Введите сообщение (для личного сообщения введите '@никнейм сообщение'): ")
            client_socket.sendall(message.encode())
    except ConnectionRefusedError:
        print("[SERVER] Сервер не доступен.")
    except KeyboardInterrupt:
        client_socket.close()

start_client()

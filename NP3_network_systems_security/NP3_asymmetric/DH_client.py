import socket
import random


def generate_key(p, g, b):
    return pow(g, b, p)


def main():
    # Задаем параметры p и g
    p = 23
    g = 5

    # Генерируем случайное число b
    b = random.randint(1, p - 1)

    # Создаем сокет и подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Получаем от сервера параметры p и g
    p = int(client_socket.recv(1024).decode())
    g = int(client_socket.recv(1024).decode())

    # Вычисляем значение g^b mod p и отправляем его серверу
    gb = generate_key(p, g, b)
    client_socket.sendall(str(gb).encode())

    # Шифруем сообщение и отправляем его серверу
    message = 'Hello, server!'
    encrypted_message = ''.join([chr(ord(c) + gb) for c in message])
    client_socket.sendall(encrypted_message.encode())

    # Получаем ответ от сервера и расшифровываем его
    response = client_socket.recv(1024).decode()
    decrypted_response = ''.join([chr(ord(c) - gb) for c in response])
    print(decrypted_response)

    # Закрываем соединение
    client_socket.close()


if __name__ == '__main__':
    main()
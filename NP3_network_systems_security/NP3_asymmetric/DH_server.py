import socket
import random

def generate(p, g, a):
    return pow(g, a, p)

def main():
    # Задаем параметры p и g
    p = 23
    g = 5

    # Генерируем случайное число a
    a = random.randint(1, p - 1)

    # Создаем сокет и начинаем прослушивание
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    # Принимаем соединение от клиента
    client_socket, address = server_socket.accept()

    # Отправляем клиенту параметры p и g
    client_socket.sendall(str(p).encode())
    client_socket.sendall(str(g).encode())

    # Получаем от клиента значение g^b mod p
    gb = int(client_socket.recv(1024).decode())

    # Вычисляем общий секретный ключ
    key = generate_key(p, gb, a)

    # Шифруем сообщение от клиента и отправляем его обратно
    message = client_socket.recv(1024).decode()
    encrypted_message = ''.join([chr(ord(c) + key) for c in message])
    client_socket.sendall(encrypted_message.encode())

    # Закрываем соединение
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
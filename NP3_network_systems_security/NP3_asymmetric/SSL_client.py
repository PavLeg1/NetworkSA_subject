import socket
import ssl

def main():
    # Создаем сокет и подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Создаем SSL контекст
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.load_verify_locations(cafile='server.crt')

    # Оборачиваем сокет в SSL соединение
    ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname='localhost')

    # Отправляем сообщение серверу и получаем ответ
    message = 'Hello, server!'
    ssl_socket.sendall(message.encode())
    response = ssl_socket.recv(1024).decode()

    # Выводим ответ на экран
    print(response)

    # Закрываем соединение
    ssl_socket.close()

if __name__ == '__main__':
    main()
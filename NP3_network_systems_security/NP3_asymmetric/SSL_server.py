import socket
import ssl

def main():
    # Создаем сокет и начинаем прослушивание
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    # Принимаем соединение от клиента
    client_socket, address = server_socket.accept()

    # Создаем контекст
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    # Оборачиваем сокет в SSL соединение
    ssl_socket = ssl_context.wrap_socket(client_socket, server_side=True)

    # Получаем сообщение от клиента и отправляем его обратно
    message = ssl_socket.recv(1024).decode()
    ssl_socket.sendall(message.encode())

    # Закрываем соединение
    ssl_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
# Простой сервер с реализацией модуля asynchio

import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Получено {message!r} от {addr!r}")

    writer.write(data)
    await writer.drain()

    print(f"Отправлено {message!r} обратно {addr!r}")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 9090)

    addr = server.sockets[0].getsockname()
    print(f"Сервер запущен на {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())
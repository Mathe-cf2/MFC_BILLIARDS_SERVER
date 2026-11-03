
import asyncio
import os
import http

from websockets.asyncio.server import serve


async def servidor(websocket):
    print("Novo jogador conectado!")

    try:
        async for mensagem in websocket:
            print(f"Mensagem recebida: {mensagem}")
            await websocket.send(f"Servidor recebeu: {mensagem}")

    except Exception as erro:
        print(f"Conexão encerrada: {erro}")


def health_check(connection, request):
    if request.path == "/healthz":
        return connection.respond(http.HTTPStatus.OK, "OK\n")


async def main():
    porta = int(os.environ.get("PORT", 10000))

    async with serve(
        servidor,
        "0.0.0.0",
        porta,
        process_request=health_check
    ) as server:

        print(f"MFC BILLIARDS online na porta {porta}!")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

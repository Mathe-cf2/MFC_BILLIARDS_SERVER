import asyncio
import websockets

async def servidor(websocket):
    print("Novo jogador conectado!")

    try:
        async for mensagem in websocket:
            print(f"Mensagem recebida: {mensagem}")

            await websocket.send(
                f"Servidor recebeu: {mensagem}"
            )

    except websockets.exceptions.ConnectionClosed:
        print("Jogador desconectado!")


async def main():
    async with websockets.serve(
        servidor,
        "0.0.0.0",
        10000
    ):
        print("Servidor MFC BILLIARDS iniciado!")
        await asyncio.Future()


asyncio.run(main())
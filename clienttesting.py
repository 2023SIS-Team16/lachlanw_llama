#This file is for having a client to interact with the server WS
import websockets
import asyncio

async def connect():
    async with websockets.connect('ws://localhost:8000') as ws:
        print("Client Connected")
        await ws.send("Parse: h ello there my fend")
        res = await ws.recv()
        print(res)

asyncio.get_event_loop().run_until_complete(connect())
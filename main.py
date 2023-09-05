import conversion
import asyncio
import websockets
from llama_cpp import Llama
model = Llama(model_path="./model/codellama-13b.Q2_K.gguf") #Replace with whatever model you are using

async def req_handler(websocket, path):
    data = await websocket.recv()
    data = data[7:]
    print(data)
    res = conversion.get_response(data, model)
    print(res)
    await websocket.send(res)
    
#Running the server
print("Server starting.")
server = websockets.serve(req_handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
print("This shouldn't run.")
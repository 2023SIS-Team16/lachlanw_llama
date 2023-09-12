import conversion
import asyncio
import websockets
from llama_cpp import Llama
model = Llama(model_path="./model/codellama-13b.Q5_K_M.gguf") #Replace with whatever model you are using

async def req_handler(websocket, path):
    data = await websocket.recv() #Wait for a translation request
    data = data[7:] #Filter out the request's preamble
    print(data)
    res = conversion.get_response(data, model)
    print(res)

    #Check if the conversion passed or failed.
    if res == data:
        await websocket.send(f"FAIL: {res}")
    else:
        await websocket.send(f"PASS: {res}")
    
#Running the server
print("Server starting.")
server = websockets.serve(req_handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
print("This shouldn't run.")
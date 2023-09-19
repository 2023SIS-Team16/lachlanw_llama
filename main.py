from http.server import BaseHTTPRequestHandler, HTTPServer
from llama_cpp import Llama
model = Llama(model_path="./model/codellama-13b.Q5_K_M.gguf") #Replace with whatever model you are using

#New server (child of BaseHTTPRequestHandler)
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
            self.send_response(200)

if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8080), Server)


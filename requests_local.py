import requests
import json
import conversion
from llama_cpp import Llama

model = Llama(model_path="./model/codellama-13b.Q5_K_M.gguf") #Replace with whatever model you are using

#Request Translation - Return String
def request_translation(text):    
    response =  conversion.get_response(text, model, keep_punctuation=False, enable_logging=True)

    print(f"Response: {response}")

    return response
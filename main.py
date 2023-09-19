import conversion
from flask import Flask, request
from llama_cpp import Llama
#model = Llama(model_path="./model/codellama-13b.Q5_K_M.gguf") #Replace with whatever model you are using
app = Flask(__name__)

@app.route("/parse_text")
def parse_text():
    data = request.get_json()
    
    print(data['text']) #data.text - The full text sent from the client
    print(data['index']) #data.resolved_index - All characters preceding this index have already been 'fixed' and returned

    #Try and find a 'sentence' to translate
    #If there's >30 characters between index and text length, try and cut it off with a space
    #If this reaches >85 (without an enabling space), force a hard cutoff

    response = {}
    response['text'] = "after processing" #Translated text
    response['status'] = False #Returns if the translation passed or failed. Optional parameter
    response['index'] = 42 #The index after this response. Changes from req's index if translation occured

    print(response)

    return response


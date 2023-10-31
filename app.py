import translator.conversion as conversion
from flask import Flask, request
from llama_cpp import Llama
import json
model = Llama(model_path="./model/codellama-13b.Q5_K_M.gguf") #Replace with whatever model you are using
app = Flask(__name__)

@app.route("/parse_text")
def parse_text():
    data = request.get_json()
    data = json.loads(data)

    print(data['text']) #data.text - The full text sent from the client
    print(data['index']) #data.resolved_index - All characters preceding this index have already been 'fixed' and returned
    diff = len(data['text']) - data['index']
    print(f"Difference: {diff}")

    response = {}
    #response['text'] = "after processing" #Translated text
    #response['status'] = False #Returns if the translation passed or failed. Optional parameter
    response['index'] = data['index'] #The index after this response. Changes from req's index if translation occured

    #Try and find a 'sentence' to translate
    #If there's >30 characters between index and text length, try and cut it off with a space
    #If this reaches >85 (without an enabling space), force a hard cutoff
    if diff <= 15:
        return response
    
    to_process = data['text'][data['index']:]
    print(to_process)

    last_index = to_process.rfind(' ')

    #Only try to cut out unfinished words if the request wants it
    if data['truncate'] == True:
        if last_index >= 15 and last_index != -1: #Cut off the text after the last space, if it exists and isn't three letters in
            to_process = to_process[:last_index] #Cut off by the last space
        elif diff < 85:
            return response #Don't try to translate unless its getting too long
    
    response['index'] += len(to_process)

    processed = conversion.get_response(to_process, model, enable_logging=True)
    print(processed)
    response['text'] = processed
    if to_process == processed:
        response['status'] = False
    else:
        response['status'] = True
    return response

if __name__ == "__main__":
    app.run(debug=True)
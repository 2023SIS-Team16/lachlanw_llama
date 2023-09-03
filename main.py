from llama_cpp import Llama
model = Llama(model_path="./model/codellama-13b.Q2_K.gguf") #Replace with whatever model you are using
def get_response(to_fix):
    response = model(f"Q: What is the correct spelling of '{to_fix}' A:", stop=["Q:", "\n"], max_tokens=32, echo=True)
    
    result = response['choices'][0]['text']

    end_index = len(to_fix) + 40
    result = result[end_index:].strip()
    

    print(to_fix)
    print(result)

    if len(to_fix) * 1.5 < len(result) or len(to_fix) * 0.8 > len(result):
        return to_fix #Just return original string if the response dramatically alters the sentence's length #TODO: Possibly check the similarity of the characters
    else:
        return result #Return fixed string


print(get_response("What ae you d ing"))
print(get_response("Hmllo there!"))
print(get_response("Ye s I think so"))
print(get_response("My name is Lchlan"))
print(get_response("Are yousure about tht"))

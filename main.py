from llama_cpp import Llama

model = Llama(model_path="./model/codellama-13b.Q2_K.gguf") #Replace with whatever model you are using

to_fix = "What ae you dxing"

output = model("Q: Who is the prime minister of Australia? A:", max_tokens=8, echo=True)
#output = model(f"Break the following into several grammatically correct words, correcting spelling errors: '{to_fix}' ", max_tokens=32, stop=["Break", "\n"], echo=True)
print(output)
print("TEST")
#Error caused by using GGML3 version instead of GGUF

def get_response(to_fix):
    print("TODO!")
    response = model(f"Break the following into several grammatically correct words, correcting spelling errors: '{to_fix}' ", max_tokens=32, stop=["Q:", "\n"], echo=True)
    return response

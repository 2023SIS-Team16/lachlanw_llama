from llama_cpp import Llama
model = Llama(model_path="./model/codellama-13b.Q2_K.gguf") #Replace with whatever model you are using
def get_response(to_fix):
    print("TODO!")
    response = model(f"Q: What is the correct spelling of '{to_fix}' A:", stop=["Q:", "\n"], max_tokens=8, echo=True)
    to_remove = f"Q: What is the correct spelling of '{to_fix}' A:"
    print(response)
    result = response['choices'][0]['text']

    print(result)
    end_index = len(to_fix) + 40
    result = result[end_index:].strip().strip("'")

    return result

to_fix = "What ae you dxing"

print(get_response("What ae you d ing"))


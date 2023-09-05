import conversion
from llama_cpp import Llama
model = Llama(model_path="model/codellama-13b.Q2_K.gguf") #Replace with whatever model you are using

print(conversion.get_response("what ae you d ing", model))
print(conversion.get_response("hmllo there", model))
print(conversion.get_response("yesi think so", model))
print(conversion.get_response("my name is lchlan", model))
print(conversion.get_response("are yousu re about tht", model))
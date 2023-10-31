import translator.conversion as conversion
from flask import Flask, request
from llama_cpp import Llama
import json
import os
from dotenv import load_dotenv
import openai
app = Flask(__name__)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print(os.getenv("OPENAI_API_KEY"))

print("STARTING TEST")
print(conversion.get_response("how are ymu doing", openai, enable_logging=True))
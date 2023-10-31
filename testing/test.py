import sys
sys.path.append("..")
from translator import conversion
from llama_cpp import Llama
import unittest

import translator.conversion as conversion
from flask import Flask, request
from llama_cpp import Llama
import json
import os
from dotenv import load_dotenv
import openai
app = Flask(__name__)
import time


""" def compare_strings(unittest, input, expected):
    output = conversion.get_response(input, model)
    unittest.assertEqual(output, expected) """

class TestConversion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        cls.model = openai

    def compare_strings(self, input, expected):
        print(f"Input: {input}")
        print(f"Expected: {expected}")
        output = conversion.get_response(input, self.model, enable_logging=False)
        print(f"Output: {output}")
        time.sleep(10)
        self.assertEqual(output, expected)

    def test_get_response_normal_case(self):
        self.compare_strings("hxllo there", "hello there")
        
    def test_get_response_normal_case_2(self):
        self.compare_strings("how afe you", "how are you")

    def test_get_response_normal_case_3(self):
        self.compare_strings("the wether is nice today", "the weather is nice today")

    def test_get_response_multiple_typos_case(self):
        self.compare_strings("wh t ae you d ing", "what are you doing")

    def test_get_response_confused_letters(self):
        self.compare_strings("m and n are oftem comfused in asl", "m and n are often confused in asl")

    def test_get_response_confused_letters_2(self):
        self.compare_strings("in a big fam of tranpolimes", "im a big fan of trampolines")

    def test_get_response_confused_letters_with_typo(self):
        self.compare_strings("i thimk itis rather innocent", "i think it is rather innocent")

    def test_get_response_confused_letters_with_typo_2(self):
        self.compare_strings("thpt is absolmtely wrong", "that is absolutely wrong")

    def test_get_response_no_spacing(self):
        self.compare_strings("theweatherisnicetoday", "the weather is nice today")

    def test_get_response_no_spacing_2(self):
        self.compare_strings("thissentencehasnospaces", "this sentence has no spaces")

    def test_get_response_homophones(self):
        self.compare_strings("they're going two the store", "theyre going to the store")

    def test_get_response_homophones_2(self):
        self.compare_strings("its a nice whether today", "its a nice weather today")

    def test_get_response_homophones_3(self):
        self.compare_strings("you're advise was helpful", "your advice was helpful")

    def test_get_response_missed_keys(self):
        self.compare_strings("hats up", "whats up")

    def test_get_response_missed_keys_2(self):
        self.compare_strings("how dod you do that", "how did you do that")

    def test_get_response_misplaced_space(self):
        self.compare_strings("I lik e chocolate", "i like chocolate")

    def test_get_response_double_typing(self):
        self.compare_strings("I amm going home", "i am going home")

    def test_get_response_uppercase_error(self):
        self.compare_strings("i love pARIS in the springtime", "i love paris in the springtime")

    def test_get_response_dropped_vowel(self):
        self.compare_strings("somtimes it happens", "sometimes it happens")  

if __name__ == '__main__':
    unittest.main()
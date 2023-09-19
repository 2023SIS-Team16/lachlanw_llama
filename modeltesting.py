import conversion
from llama_cpp import Llama
import unittest

""" def compare_strings(unittest, input, expected):
    output = conversion.get_response(input, model)
    unittest.assertEqual(output, expected) """

class TestConversion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = Llama(model_path="./model/codellama-13b.Q5_K_M.gguf")

    def compare_strings(self, input, expected):
        output = conversion.get_response(input, self.model)
        self.assertEqual(output, expected)

    def test_get_response_normal_case(self):
        self.compare_strings("hmllo there", "hello there")
        
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

if __name__ == '__main__':
    unittest.main()

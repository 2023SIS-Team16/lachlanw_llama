import conversion
from llama_cpp import Llama
import unittest

class TestConversion(unittest.TestCase):
    
    def setUp(self):
        self.model = Llama(model_path="./model/codellama-13b.Q2_K.gguf")

    def test_get_response_normal_case(self):
        # Arrange
        input_str = "hmllo there"
        expected_output = "hello there"

        # Act
        actual_output = conversion.get_response(input_str, self.model)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_get_response_edge_case(self):
        # Arrange
        input_str = "wh t ae you d ing"
        expected_output = "what are you doing"

        # Act
        actual_output = conversion.get_response(input_str, self.model)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_get_response_asl_confusion(self):
        # Arrange
        input_str = "m and n are oftem comfused in asl"
        expected_output = "m and n are often confused in asl"

        # Act
        actual_output = conversion.get_response(input_str, self.model)

        # Assert
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()

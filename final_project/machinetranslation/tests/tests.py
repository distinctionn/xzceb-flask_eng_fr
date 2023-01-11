import unittest
from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    def test_english_to_french_null_input(self):
        englishText = None
        self.assertRaises(TypeError, translator.english_to_french, englishText)
        
    def test_french_to_english_null_input(self):
        frenchText = None
        self.assertRaises(TypeError, translator.french_to_english, frenchText)

    def test_hello_translation(self):
        englishText = "Hello"
        frenchText = translator.english_to_french(englishText)
        self.assertEqual(frenchText, "Bonjour")

    def test_bonjour_translation(self):
        frenchText = "Bonjour"
        englishText = translator.french_to_english(frenchText)
        self.assertEqual(englishText, "Hello")

if __name__ == '__main__':
    unittest.main()

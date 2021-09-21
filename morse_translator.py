"""
Author : https://github.com/Hatcattt

MorseTranslatorPy

- This program can translate Morse code into text,
  and vice versa.

- The Morse code is in a csv file
- The csv module is used

- Morse code letters are separated with / slash
"""

import csv
import unittest

FILE = "File/morse_code.csv"

with open(FILE) as f:
    f.readline()  # no need the first line

    # create a dictionary with character as key, code as value.
    MORSE_DICO = dict(filter(None, csv.reader(f)))
    f.close()

# reverse the dictionary
MORSE_DICO_REVERSE = {value: key for key, value in MORSE_DICO.items()}


def translate_into_morse(text):
    """
    Translate a text message to Morse code.
    :param text: message to transform (string)
    :return: message in Morse code (string)
    """
    result = ""
    for char in text.lower():
        try:
            result += "/ " if char == " " else MORSE_DICO[char] + " "
        except KeyError:
            result += "# "  # key not found
    return result[:len(result)-1]


def translate_morse(message):
    """
    Translate a Morse code to text message.
    :param message: Morse code (string)
    :return: message in text (string)
    """
    result = ""
    for code in message.split(" "):
        try:
            result += " " if code == "/" else MORSE_DICO_REVERSE[code]
        except KeyError:
            result += "" if not message else "#"
    return result.upper()


# TESTING
class TestMorseTranslatorPy(unittest.TestCase):
    # TEXT TO MORSE CODE
    def test_text_into_morse_code(self):
        result = translate_into_morse("hello")
        self.assertEqual(".... . .-.. .-.. ---", result)

    def test_empty_text_into_morse_code(self):
        result = translate_into_morse("")
        self.assertEqual("", result)

    def test_only_one_space_text_into_morse_code(self):
        result = translate_into_morse(" ")
        self.assertEqual("/", result)

    def test_text_with_space_into_morse_code(self):
        result = translate_into_morse("hello world !")
        self.assertEqual(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / -.-.--", result)

    def test_bad_text_into_morse_code(self):
        result = translate_into_morse("hello & world")  # key '&' not in dictionary
        self.assertEqual(".... . .-.. .-.. --- / # / .-- --- .-. .-.. -..", result)

    # MORSE CODE TO TEXT
    def test_morse_code_to_text(self):
        result = translate_morse(".... . .-.. .-.. ---")
        self.assertEqual("HELLO", result)

    def test_empty_morse_code_to_text(self):
        result = translate_morse("")
        self.assertEqual("", result)

    def test_morse_code_with_space_to_text(self):
        result = translate_morse(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        self.assertEqual("HELLO WORLD", result)

    def test_bad_morse_code_to_text(self):
        result = translate_morse(".... . .-.. .-.. --- / .-- BUG .-. .-.. -..")
        self.assertEqual("HELLO W#RLD", result)


if __name__ == '__main__':
    unittest.main()

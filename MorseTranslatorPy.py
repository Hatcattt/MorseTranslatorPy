"""
Author : https://github.com/Hatcattt

Morse-TranslatorPy

- This program can translate Morse code into text,
  and vice versa.

- The Morse code is in a csv file
- The csv module is used

- Morse code letters are separated with / slash
"""

import csv

file = "morse_code.csv"

with open(file) as f:
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
            result += "# "
    return result.upper()


# Text to morse code
sentence = "Hello there !"
morse_message = translate_into_morse(sentence)

# Morse code to text
morse_sentence = "- .... .- -. -.- ... / ..-. --- .-. / - . ... - .. -. --. / -.-.--"
new_sentence = translate_morse(morse_sentence)

print(f"Original sentence => {sentence}\n"
      f"Final Morse code  => {morse_message}\n")

print(f"Original Morse code => {morse_sentence}\n"
      f"Final sentence      => {new_sentence}")

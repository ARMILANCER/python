from collections import OrderedDict
from itertools import cycle
import string

# position of alfabet
def deCode(character):
    if character.islower():
        charKey = next(key_cycle)
        return string.ascii_lowercase[((ord(character)-ord('a'))+(ord(charKey.lower())-ord('a')))%26]
    if character.isupper():
        charKey = next(key_cycle)
        return string.ascii_uppercase[((ord(character)-ord('A'))+(ord(charKey.upper())-ord('A')))%26]
    else: return character

# this funtion counts number of repetitions
def counter():
    for character in text:
        if character.isalpha():
            character = character.lower()
        if character in frequenze:
            frequenze[character] += 1
        else: frequenze[character] = 1
    for key,value in frequenze.items():
        print(f"Key: {key}, Value: {value}")
        
        
# type Hash map, contain letters and counters
frequenze = OrderedDict()
# Contain the encoded text
textCode = ""
# Contain the decoded text
texToDecod = ""

text = input("Inserisce il Testo: ")
key = input("Key: ")

key_cycle = cycle(key)
for character in text:
    textCode += deCode(character)
print(textCode)

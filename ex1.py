
texToDecod = ""
key = int(input("Key: "))
texToCod = str(input("Stringa: "))

for character in texToCod:
    if ord(character)==32:
        texToDecod += character
        print(end=" ")
    elif ord(character)>(122-key):
        print(chr(ord(character)-(122-key)),end="")
        texToDecod += chr(ord(character)-(122-key))
    else:
        print(chr(ord(character)+key),end="")
        texToDecod += chr(ord(character)+key)
           
print ("\nText decoding")

for character in texToDecod:
    if ord(character)==32:
        texToDecod += character
        print(end=" ")
    elif ord(character)>(122+key):
        print(chr(ord(character)+(122-key)),end="")
        texToDecod += character
    else:
        print(chr(ord(character)-key),end="")
        texToDecod += character


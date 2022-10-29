from string import ascii_lowercase as abc


alphabates = abc
def encrypt(text, shift):
    encrypted = ''
    for character in text:
        if character not in alphabates:
            encrypted += character
        else:
            idx = alphabates.index(character)
            new_idx = (idx + shift) % 26
            new_character = alphabates[new_idx]
            encrypted += new_character
            
    print("The encoded text is ", encrypted)


def decrypt():
    pass

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)

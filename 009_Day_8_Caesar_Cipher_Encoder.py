from string import ascii_lowercase as abc

alphabates = abc

def encrypt(plain_text, to_shift):
    encrypted = ''
    for character in plain_text:
        if character not in alphabates:
            encrypted += character
        else:
            idx = alphabates.index(character)
            new_idx = (idx + to_shift) % 26
            new_character = alphabates[new_idx]
            encrypted += new_character         
    print("The encoded text is ", encrypted)


def decrypt(encrypted_text, to_shift_back):
    decrypted = ''
    for character in encrypted_text:
        if character not in alphabates:
            decrypted += character
        else:
            idx = alphabates.index(character)
            new_idx = idx - to_shift_back
            new_character = alphabates[new_idx]
            decrypted += new_character
    print("The decoded text is ", decrypted)


direction = input("Choose (1) to encrypt, type (0) to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == '1':
    encrypt(plain_text = text, to_shift = shift)
elif direction == '0':
    decrypt(encrypted_text = text, to_shift_back=shift)
else:
    print("Invalid!! Choose 1 or 0")
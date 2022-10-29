from string import ascii_lowercase as abc

alphabates = abc

def cipher(to_cipher_text, to_shift, enc_dec):
    cipher_text = ''
    if enc_dec == "decode":
        to_shift *= -1

    for letter in to_cipher_text:
        if letter not in alphabates:
            cipher_text += letter
        else:
            idx = alphabates.index(letter)
            new_idx = (idx + to_shift) % 26
            cipher_text += alphabates[new_idx]   
    print(f"The {enc_dec}d text is --> {cipher_text} <--")


# MAIN 
def main_menu():
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(to_cipher_text=text, to_shift=shift, enc_dec=direction)

    again = input("\nType 'yes' to restart, type 'no' to exit: ").lower()
    if again == "yes":
        main_menu()
    else:
        print("End of Caesar Cipher !!")
            

main_menu()
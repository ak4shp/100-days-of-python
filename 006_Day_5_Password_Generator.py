#Password Generator Project
import random
from string import ascii_lowercase as abc, ascii_uppercase as ABC

letters = tuple(abc) + tuple(ABC)
numbers = tuple(map(str, range(10)))
symbols = ('!', '@','#', '$', '-', '&', '_', '*', '+')

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = nzoC#*10

easy_password = ''
for letter in range(nr_letters):
    easy_password += random.choice(letters)
    
for symbol in range(nr_symbols):
    easy_password += random.choice(symbols)

for number in range(nr_numbers):
    easy_password += random.choice(numbers)
    
print("easy pass:", easy_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = m8MND2+(
'''Raw method'''

letter_number = letters + numbers
letter_symbol = letters + symbols
number_symbol = numbers + symbols
letter_number_symbol = letter_number + symbols

hard_pass = ''

n = nr_letters + nr_numbers + nr_symbols
for i in range(n):
    
    #Choose from the right list
    if nr_letters > 0:
        if nr_numbers > 0:
            if nr_symbols > 0:
                r = random.choice(letter_number_symbol)
            else:
                r = random.choice(letter_number)      
        elif nr_symbols > 0:
            r = random.choice(letter_symbol) 
        else:
            r = random.choice(letters)
            
    elif nr_numbers > 0:
        if nr_symbols > 0:
            r = random.choice(number_symbol)
        else:
            r = random.choice(numbers)
            
    elif nr_symbols > 0:
        r = random.choice(symbols)
        
    #Keeping track of used letters, symbols or numbers
    if r in letters:
        nr_letters -= 1
    elif r in numbers:
        nr_numbers -= 1
    elif r in symbols:
        nr_symbols -= 1
    
    #Append the random letter, number or symbol to password string
    hard_pass += r

print("hard pass:", hard_pass)

#Hard password by shuffling easy password
#e.g. 4 letter, 2 symbol, 2 number = #C0o*nz1
'''Easy way to generate hard password'''
hard_pass_easy_way = list(easy_password)
random.shuffle(hard_pass_easy_way)

hard_pass2 = ''
for character in hard_pass_easy_way:
    hard_pass2 += character
    
#print("2nd hard pass:", hard_pass2)

    
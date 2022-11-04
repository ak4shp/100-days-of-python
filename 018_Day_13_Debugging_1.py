############ To Debug #####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

############ Debugged #####################

# # Describe Problem
def my_function():
  for i in range(1, 21): # End Range is not inclusive
    if i == 20:
      print("You got it")
my_function()


############ To Debug #####################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

############ Debugged #####################

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # Array is zero indexed.
print(dice_imgs[dice_num]) 


############ To Debug #####################

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

############ Debugged #####################

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:  #What about 1994 huh??
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")


############ To Debug #####################
# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

############ Debugged #####################

# # Fix the Errors
age = int(input("How old are you?")) # age is 'int'
if age > 18:
    print(f"You can drive at age {age}.") #indentation, F-string


############ To Debug #####################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

############ Debugged #####################

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #use '=' for asignment '==' for comparision
total_words = pages * word_per_page
print(total_words)


############ To Debug #####################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

############ Debugged #####################

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)  # This operation is inside loop, so indent it
  print(b_list)

mutate([1,2,3,5,8,13])


# Next Tip -> Take a break

# Next Tip -> Ask a friend or mentor or someone who knows code.

# Next Tip -> Run Often your code even you make small change. Dont save for the end.

# Next Tip -> Use stackoverflow.

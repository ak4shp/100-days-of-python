# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = (name1 + name2).lower()

left_count = name.count("t")
left_count += name.count("r")
left_count += name.count("u")
left_count += name.count("e")

right_count = name.count("l")
right_count += name.count("o")
right_count += name.count("v")
right_count += name.count("e")

number = int(str(left_count) + str(right_count))

if number < 10 or number > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif number >=40 and number <= 50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.") 




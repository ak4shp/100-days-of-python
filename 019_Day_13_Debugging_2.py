# Even-odd number : fix the bug

number = int(input("Which number do you want to check?"))

if number % 2 == 0: # Bug was here. '=' is given, '==' needed
  print("This is an even number.")
else:
  print("This is an odd number.")


# Leap-year : fix the bug
  
year = int(input("Which year do you want to check?"))
#Bug: year was string, casted to int.
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


# FizzBuzz : fix the bugs

for number in range(1, 101):
#bug1: logic -> if-nested_if-elif-else not if-if-if-else
  if number % 3 == 0:
      if number % 5 == 0:
        print("FizzBuzz")
      else:
        print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) #bug2: unneccesary [] in numbers. '[numbers]' -> 'numbers'.
  
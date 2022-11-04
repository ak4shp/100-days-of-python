# Even-odd number : fix the bug

number = int(input("Which number do you want to check?"))

if number % 2 == 0: # Bug was here. '=' is given, '==' needed
  print("This is an even number.")
else:
  print("This is an odd number.")


  
  

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip/100)
payable = total_bill / people
final_amount = "{:.2f}".format(payable)
print(f"Each person should pay: ${final_amount}")
print(type(final_amount))
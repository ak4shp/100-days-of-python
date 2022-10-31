
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# # key -> symbol, value -> operation function
# operations = {
#     "+" : add,
#     "-" : subtract,
#     "*" : multiply,
#     "/" : divide
# }


# # Ask for first num and Print all symbols for UX
# num1 = int(input("First number? "))
# for symbol in operations:
#     print(symbol)

# # Continuing calculation
# more_calculation = True
# while more_calculation:
#     operation_symbol = input("\nWhich operation?  ")
#     num2 = int(input("Next number? "))
#     calculation_function = operations[operation_symbol] #Uses dict's key|value to do asked operation
#     ans = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {ans}")
#     num1 = ans

#     more_operation = input(f"Type 'y' to continue calculating with {ans}, or press any key to exit.: ").lower()
#     if more_operation == 'y':
#         continue
#     else:
#         print("Final result is: ", ans)
#         more_calculation = False    
    

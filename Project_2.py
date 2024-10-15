# Get the first number from the user
operand = input("Number 1: ")

# Get the second number from the user
operand2 = input("Number 2: ")

# Get the operation sign from the user
sign = input("Sign: ")

# Initialize a flag to check if the input is valid
valid = False

# Try to convert the inputs to floats
try:
    operand = float(operand)
    operand2 = float(operand2)
    valid = True
except:
    # If conversion fails, print an error message
    print("Invalid input")

# Try and Catch Exceptions
try:
    # Convert the inputs to floats again (redundant, can be removed)
    operant = float(operand)
    operant2 = float(operand2)
except:
    # If conversion fails, print an error message and exit
    print("You must enter a number")
    exit()

# Initialize the result variable
result = 0

# Perform the operation based on the sign
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "*":
    result = operand * operand2
elif sign == "/":
    # Check for division by zero
    if operand2 == 0:
        result = "You can't divide by 0"
    else:
        result = operand / operand2

# Print the result
print(result)
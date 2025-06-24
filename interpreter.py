#In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.

#For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

#x is an integer
#y is +, -, *, or /
#z is an integer


# Prompt the user for an arithmetic expression
expression = input("Enter expression (e.g. 1 + 1): ")

# Split the input into its parts
x, operator, z = expression.split()

# Convert x and z to integers
x = int(x)
z = int(z)

# Compute the result based on the operator
if operator == '+':
    result = x + z
elif operator == '-':
    result = x - z
elif operator == '*':
    result = x * z
elif operator == '/':
    result = x / z

# Output the result as a floating-point number formatted to one decimal place
print(f"{result:.1f}")

# This program prompts the user for an arithmetic expression and calculates the result.2+




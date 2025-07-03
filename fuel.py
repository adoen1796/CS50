#FUEL GAUGE PROBLEM

#Fuel gauges indicate, often with fractions, 
# just how much fuel is in a tank. 
# For instance 1/4 indicates that a tank 
# is 25% full, 1/2 indicates that a tank is 50% full, 
# and 3/4 indicates that a tank is 75% full.

#In a file called fuel.py,
#  implement a program that prompts the user for a fraction, 
# formatted as X/Y, wherein each of X and Y is a positive integer,
#  and then outputs, as a percentage rounded to the nearest integer,}
#  how much fuel is in the tank. If, though, 1% or less remains, output
#  E instead to indicate that the tank is essentially empty. And if 99% or more
#  remains, output F instead to indicate that the tank is essentially full.

x= int(input("Qty of fuel in tank: "))
y= int(input("Total capacity of tank: "))

try:
    fraction = x / y
    percentage = round(fraction * 100)

    if x>y:
        print("Error: Quantity cannot exceed capacity.")
    elif percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")
except Zero20DivisionError:
    print("Error: Total capacity cannot be zero.")
except ValueError:
    print("Error: Please enter valid integers for quantity and capacity.")


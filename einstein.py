#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
#FOR E=MC2 OF EINTSTEIN 

c=300000000
m=int(input("Enter the mass in kilograms: "))

e=round(m*c**2,2)

print(f"The equivalent energy in Joules is: {e} J")
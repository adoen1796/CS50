#In a file called adieu.py, implement a program that prompts the user for names, 
# one per line, until the user inputs control-d. Assume that the user will input at least one name.
#  Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 #names with 
# commas and one and, as in the below:


def main():
    names = []

    # Captura de nombres hasta Control-D (EOF)
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()  # Salto de línea después de EOF

    # Construcción del mensaje
    message = "Adieu, adieu, to "

    if len(names) == 1:
        message += names[0]
    elif len(names) == 2:
        message += f"{names[0]} and {names[1]}"
    else:
        message += ", ".join(names[:-1])
        message += f", and {names[-1]}"

    print(message)

if __name__ == "__main__":
    main()





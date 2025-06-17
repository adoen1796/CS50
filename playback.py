#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

Text_input = str(input("Enter the text to be processed: "))
Text_output = Text_input.replace(" ", "...")

print(f"{Text_output}")


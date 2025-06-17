#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.


def convert_text(text: str) -> str:
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

#Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 
def main():

    user_input = input("Enter the text to be processed: ")
    converted_text = convert_text(user_input)
    print(converted_text)

#You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.
if __name__ == "__main__":
    main()

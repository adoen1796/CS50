#implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    if answer := input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower() in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

main()
#figlet.py

#Expects zero or two command-line arguments:
#Zero if the user would like to output text in a random font.
#Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.

import sys
import random
import pyfiglet

def main():
    args = sys.argv[1:]
    figlet = pyfiglet.Figlet()

    if len(args) == 0:
        font = random.choice(figlet.getFonts())
    elif len(args) == 2 and args[0] in ["-f", "--font"]:
        font = args[1]
        if font not in figlet.getFonts():
            sys.exit(f"Font '{font}' not available.")
        figlet.setFont(font=font)
    else:
        sys.exit("Uso correcto: python script.py [-f FUENTE]")

    user_text = input("Texto a usar: ")

    #stablish fond
    if len(args) == 0:
        figlet.setFont(font=font)

    print(figlet.renderText(user_text))

if __name__ == "__main__":
    main()




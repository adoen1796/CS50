import random

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass  # Ignora entrada no numérica

def main():
    
    level = get_positive_int("Level: ")

    # random number
    number = random.randint(1, level)
    while True:
        guess = get_positive_int("Guess: ")

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()

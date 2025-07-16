# Prompts the user for a level, 
# . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
#  digits. No need to support operations other than addition (+).
# Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y
#  pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        else:
            print(f"{x} + {y} = {x + y}")
    
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()

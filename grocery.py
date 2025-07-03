#In a file called grocery.py, 
# implement a program that prompts the user for items,
#  one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
#  Treat the user’s input case-insensitively.


items=input("Item: ").strip()
grocery_list = {}

def main():
    while True:
        try:
            item = input("Item: ").strip()
            if item == "":
                continue
            item = item.upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            break

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()
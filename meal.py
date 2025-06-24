"""
In meal.py, implement a program that 
# prompts the user for a time and outputs whether it’s breakfast time,
#  lunch time, or dinner time. If it’s not time for a meal, 
# don’t output anything at all. Assume that the user’s input
#  will be formatted in 24-hour time as #:## or ##:##. And 
# assume that each meal’s time range is inclusive. 
# For instance, 
# whether it’s 7:00, 7:01, 7:59, or 8:00, 
# or anytime in between, it’s time for breakfast.
"""

def main():
    time = input("What time is it? ").strip()
    if convert(time) == "breakfast":
        print("breakfast time")
    elif convert(time) == "lunch":
        print("lunch time")
    elif convert(time) == "dinner":
        print("dinner time")



def convert(time):
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Check the time ranges 
    if 7 <= hours < 11 or (hours == 11 and minutes == 0):
        return "breakfast"
    elif 11 <= hours < 15 or (hours == 15 and minutes == 0):
        return "lunch"
    elif 17 <= hours < 21 or (hours == 21 and minutes == 0):
        return "dinner"
    else:
        return None

if __name__ == "__main__":
    main()   
#In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month 
# in the latter might be any of the values in the list below:
#push out in way YYYY-MM-DD

months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date_input = input("Date: ").strip()
    
    # Check for format "Month Day, Year"
    if "," in date_input:
        month_str, day_year = date_input.split(",")
        month_str = month_str.strip()
        day_year = day_year.strip()
        if month_str in months:
            month = months.index(month_str) + 1
            day, year = map(int, day_year.split())
            print(f"{year:04}-{month:02}-{day:02}")
            return
    
    # Check for format "M/D/YYYY"
    try:
        month, day, year = map(int, date_input.split("/"))
        print(f"{year:04}-{month:02}-{day:02}")
    except ValueError:
        print("Invalid date format. Please use 'Month Day, Year' or 'M/D/YYYY'.")
if __name__ == "__main__":
    main()
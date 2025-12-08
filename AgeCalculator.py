# ...existing code...
from datetime import date

try:
    # Ask user for details
    birth_year = int(input("Enter your birth year (yyyy): "))
    birth_month = int(input("Enter your birth month (mm): "))
    birth_day = int(input("Enter your birth day (dd): "))

    # validate by constructing a date (will raise ValueError for invalid dates)
    birth = date(birth_year, birth_month, birth_day)
    today = date.today()

    if birth > today:
        print("Birth date is in the future. Please enter a valid past date.")
    else:
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        print("Your age is:", age)

except ValueError:
    print("Invalid input. Please enter numeric year/month/day and a valid calendar date.")
# ...existing code...
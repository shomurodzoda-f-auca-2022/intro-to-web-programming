import calendar

def monthCalendar(year, month):
    print(calendar.month(year, month))

while True:
    try:
        year = int(input("Enter the year: "))
        if year == 0: # 0 is a sign of end input
            break

        if year < 0:
            raise ValueError("Year cannot be negative. Please try again.\n")
        month = int(input("Enter the month: "))
        if month < 1 or month > 12:
            raise ValueError("Invalid input of month, must be between 1 - 12. Please try again.\n")
    except ValueError as e:
        print(e)
        continue

    print() # an empty line for making the calendar more visible
    monthCalendar(year, month)
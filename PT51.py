month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Number of days = 29")
    else:
        print("Number of days = 28")

elif month in [4, 6, 9, 11]:
    print("Number of days = 30")

else:
    print("Number of days = 31")

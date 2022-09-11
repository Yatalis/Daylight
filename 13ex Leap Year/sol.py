# Find if the year is leap year or not

isLeapYear = False
year = int(input("Enter the year: "))
if year % 100 == 0:
    if year % 400 == 0:
        isLeapYear = True
elif year % 4 == 0:
    isLeapYear = True
if isLeapYear:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
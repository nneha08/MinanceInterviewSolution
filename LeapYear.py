
# function to find if given year is leap year or not
def isleapyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                day = year%7
                extraday(day)

            else:
                print("This is not a leap year")
                closestleapyear(year)
        else:
            day = year % 7
            extraday(day)

    else:
        print("This is not a leap year")
        closestleapyear(year)

# function to find the closest leap year to a non leap year
def closestleapyear(year):
    diff = year % 4
    if diff%2==0:
        print("Closest leap year:{}".format(year-2))
        extraday((year-2)%7)
        print("Closest leap year:{}".format(year + 2))
        extraday((year + 2) % 7)
    if diff<2:
        print("Closest leap year:{}".format(year -1))
        extraday((year - 1) % 7)
    elif diff >2:
        print("Closest leap year:{}".format(year + 1))
        extraday((year + 1) % 7)

#function to  print extra day in the leap year
def extraday(day):
    if day is 0:
        print("Sunday")
    elif day is 1:
        print("Monday")
    elif day is 2:
        print("Tuesday")
    elif day is 3:
        print("Wednesday")
    elif day is 4:
        print("Thursday")
    elif day is 5:
        print("Friday")
    elif day is 6:
        print("Saturday")


year = input("Enter the year: ")
isleapyear(int(year))
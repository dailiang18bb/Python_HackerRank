def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        leap = True

    return leap


year = int(raw_input())
print is_leap(year)

#
# def is_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


#
# def is_leap(year):
#     return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

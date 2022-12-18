"""
2017 is not a leap year
1900 is a not leap year
2012 is a leap year
2000 is a leap year
A leap year is exactly divisible by 4 except for century years (years ending with 00).
The century year is a leap year only if it is perfectly divisible by 400.
"""
#yr = int(input("Enter year YYYY: "))
yr = int("2000")
flag = (str(yr).find("00", 2))
print("flag:", flag)

if flag != -1:
    print("flag is true")
    if yr%400 == 0:
        print(" yr%400")
        print("Leap year")
    else:
        print("Not Leap year")
else:
    if yr % 4 == 0:
        print("Leap year")
    else:
        print("Not Leap year")

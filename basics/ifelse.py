# Logical Operators
"""
< Less than
> Greater than
<= Less than equal
>= Greater than equal
"""

a = int(input("Type a number: "))
if a == 10:
    print("Number is equal to 10")
elif a == 20 | a == 30:
    print("Number is equal to 20 or 30")
else:
    print("Number is not equal to given values")

b = int(input("Type a number: "))
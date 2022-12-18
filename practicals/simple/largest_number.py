# Find the largest number
# -------------------------------------------------
# Pass Arguments as Input
# x1, x2, x3 = input("Enter 3 numbers: ").split(",")
# print("x1 ,x2, x3:", x1, x2, x3)
# x1 = int(x1)
# x2 = int(x2)
# x3 = int(x3)
# --------------------------------------------------
# Pass Arguments as Input
# x = list(map(int, input("Enter 3 numbers: ").split(",")))
# x1, x2, x3 = x[0], x[1], x[2]
x1, x2, x3 = map(int, input("Enter 3 numbers: ").split(","))
if x1 >= x2:
    if x1 >= x3:
        print("largest number:", x1)
    else:
        print("largest number:", x3)
else:
    if x2 >= x3:
        print("largest number:", x2)
    else:
        print("largest number:", x3)




# Check a numeric number Positive or Negative
num = int(input("Enter a number: "))
print("Entered number:", num)
if num >= 0:
    if num == 0:
        print("Zero number: ", num)
    else:
        print("Positive number: ", num)
else:
    print("Negative number: ", num)

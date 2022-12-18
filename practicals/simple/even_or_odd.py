# num = int(input("Enter a number: "))
num = 10
print("num:", num)
if (num%2) == 0:
    print("Even number:", num)
else:
    print("Odd number:", num)

# Differentiate odd and even numbers in a list
lst = [10, 15, 16, 18, 9]
global odd
odd = []
global even
even = []
for n in lst:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Odd: ", odd)
print("Even: ", even)






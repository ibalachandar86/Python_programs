"""
A positive integer greater than 1 which has no other factors except 1,
 and the number itself is called a prime number.
2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
But 6 is not prime (it is composite) since, 2 x 3 = 6.

A number should be divided only by itself:
For example 1,2,3,5,7,11 are prime numbers can be divided by only itself.
For example 6,8 can be divided by 6,8 and 2.
"""

# Program to check if a number is prime or not

num = 8

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
global flag
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

# Prime number flag check
if flag:
    print("Not a Prime Number")
else:
    print("Prime number")

# Print prime numbers in a range
min = 100
max = 1000

for i in range(100, 1000):
    flag = False
    for n in range(2, i):
        if (i % n) == 0:
            flag = True
            break
    if flag is False:
        print("Prime number:", i)







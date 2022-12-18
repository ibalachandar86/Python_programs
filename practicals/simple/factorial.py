# Factorial 5 = 5 * 4 * 3 * 2 *1 = 120

num = int(input("Enter a numer: "))

global fact
fact = 1
for n in range(1,num+1):
    fact = fact * n
print(fact)
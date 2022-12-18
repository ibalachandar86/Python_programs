# Varibles

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

Camel Case:
myVariableName = "John"

Snake Case:
my_variable_name = "John"

Pascal Case:
MyVariableName = "John"


"""

a = 10
b = "bala"
c = 10.5
d = "27"

print("a: " + str(type(a)))
print(a, b, c, d)

e = str(a)
print(e)
f = int(d)
print(f)
g = float(d)
print(g)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x + y + z) # No Automatic case created
print(x, y, z) # Automatic space ll be created

# Global Function
x1 = "viyan"
def func1(): print("x1 :" + x1)
func1()
def func2():
    x2 = "thirun"
    print("x1, y1 :" + x1 + " " + x2)
func2()

# We can create a Global function also
def func3():
        global x3
        x3 = 5
        print("Inside func3", x3)
func3()
print("Outside func3", x3)




"""
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

x = "Hello World"	str
x = 20	int
x = 20.5	float
x = 1j	complex
x = ["apple", "banana", "cherry"]	list
x = ("apple", "banana", "cherry")	tuple
x = range(6)	range
x = {"name" : "John", "age" : 36}	dict
x = {"apple", "banana", "cherry"}	set
x = frozenset({"apple", "banana", "cherry"})	frozenset
x = True	bool
x = b"Hello"	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview
x = None	NoneType

x = str("Hello World")	str
x = int(20)	int
x = float(20.5)	float
x = complex(1j)	complex
x = list(("apple", "banana", "cherry"))	list
x = tuple(("apple", "banana", "cherry"))	tuple
x = range(6)	range
x = dict(name="John", age=36)	dict
x = set(("apple", "banana", "cherry"))	set
x = frozenset(("apple", "banana", "cherry"))	frozenset
x = bool(5)	bool
x = bytes(5)	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview

"""

x1 = "ABC"  # String
x2 = 5      # Int
x3 = 5.5    # Float
x4 = 5J     # Complex

x5 = ["a", "b", "c"] # List
x6 = ("a", "b", "c") # Tuple

x7 = {"a", "b", "c"} # Set
x8 = frozenset({"a", "b", "c"}) # FrozenSet

x9 = dict(name="x", age=10) # Dict

# Int
x = 1
y = 35656222554887711
z = -3255522

# Float
x = 1.10
y = 1.0
z = -35.59
x = 35e3
y = 12E4
z = -87.7e100

# Complex
x = 3+5j
y = 5j
z = -5j

# Type Conversion
x1 = 10     # Int
y1 = 20.5   # Float
z1 = 5J     # Complex
print(float(x1))
print(int(y1))
print(complex(x1))
print(complex(y1))

import random
print(random.randrange(10,15))
print(random.randint(10,20))

# Python Casting
x = int(1)      # x will be 1
y = int(2.8)    # y will be 2
z = int("3")    # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1")   # x will be 's1'
y = str(2)      # y will be '2'
z = str(3.0)    # z will be '3.0'

# String datatype
print("++++++++++++++++++++++")

x = "balachandar"
# print("x:", x)
y = """
aasdas kasjdja
laksjdfkj skjdfjji nnkandf
"""
# print("y:", y)

z="bala chandar"
print(z[0], z[6])
for x in z: print(x)
print("len: ", len(z))

txt = "The best things in life are free!"
if "free" in txt:
    print("free string is present")
else:
    print("free string is not present")
if "bala" not in txt:
    print("bala string is not present")
else:
    print("bala string is present")






print("++++++++++++++++++++++")



























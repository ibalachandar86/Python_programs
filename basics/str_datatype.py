# Functions

# Slicing
x = "balachandar"
print("Slice x: ", x[2:5])
print("Slice x: ", x[:4])
print("Slice x: ", x[4:])
b = "Hello, World!"
print(b[-5:-2])
if x[4:8] == "chan": print("yes:",  x[4:8])

# Upper Lower Strip Capitalize Casefold
print("slice:", x[2:5])
print("upper:", x.upper())
print("lower:", x.lower())
print("strip:", x.strip())
print("title:", "balachandar bala chandar".strip().title()) # "Balachandar Bala Chandar" converts the first character of all words
print("capitalize:", " bala chandar ".strip().capitalize()) # "Bala chandar" capitalize Converts the first character to upper case
print("casefold:", " BaLa ".strip().casefold())        # casefold Converts string into lower case (Implements caseless string matching)
if "BaLa".casefold() == "bala": print("Casefold Name matching")

# Center Python String center() method creates and returns a new string that is padded with the specified character.
"""
Syntax:  string.center(length[, fillchar])
Parameters:
length: length of the string after padding with the characters.
fillchar: (optional) characters which need to be padded. If it’s not provided, space is taken as the default argument.
"""
x = "abc def gef"
print("center:",x.center(50
                         ))
print("center:",x.center(50,"x"))

"""
print(x.replace("Chandar","jwala"))             # Replace
print(x.split(" "))                             # Split
for n in x.split(" "): print(n)                 # Split Loop
print(x.strip() + "," + "rocks")                # Concatenate
print("Value {}".format(x))                     # Format
myString = "abc def {} {} {}"
print(myString.format("x","y","z"))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format("quantity", "itemno", "price"))
print("The escape charater \"Bala\" ")               # Escape Character


print("center:", "    bala chandar iyanar".strip().center(10))                  # center Returns a centered string
print("count words:", "bala bala chandar viyan bala thirun bala".count("bala")) # Return the number of times the value "apple" appears in the string
print("encode:", "bala".encode("ascii"))             # Encode
print("endswith", "bala chandar".endswith("r"))      # Endswith
print("endswith", "bala chandar".endswith("chan", 5, 9))
print("H\te\tl\tl\to".expandtabs())                  # Expand tabs
print("find:", "balachandar".find("chan"))           # Find
print("find:", "balachandar".find("c",4,5))
# 4 - Start POS 7 - End POS
"""

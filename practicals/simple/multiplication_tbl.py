num = int(input("Enter a number:"))

for n in range(1,num+1):
    mult = n * num
    print("Table {} * {} = {}".format(num,n,mult))
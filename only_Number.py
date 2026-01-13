x  = []
count = 10
for i in range(count):
    a = eval(input("Enter only int value :"))
    x.append(a)
    if type(a) == str :
        print("Value should be number")
        x.remove(a)
print(x)
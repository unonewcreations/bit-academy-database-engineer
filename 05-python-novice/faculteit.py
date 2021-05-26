num = int(input("Van welke getal wil je de faculteit weten? "))
fac = 1

if num < 0:
    print("Faculteit onder 0 kan niet")
elif num == 0:
    print("De faculteit van {num} is 1")
else:
    for i in range(1, num+1):
        fac = fac * i
    print("De faculteit van", num, "is",  fac)

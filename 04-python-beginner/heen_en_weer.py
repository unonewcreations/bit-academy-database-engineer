num = int(input("Tot welk getal? "))
start = 1
stop = num

stop += start

for i in range(start, stop):
    print(i)

for j in reversed(range(start, i)):
    print(j)

Floor = 0
Floris = 0
keuze = " "

while keuze != "UITSLAG":
    keuze = input("Op wie wil je stemmen? ")
    if keuze == "Floor":
        Floor += 1
    elif keuze == "Floris":
        Floris += 1
if Floor > Floris:
    print("Floor heeft gewonnen!")
elif Floris > Floor:
    print("Floris heeft gewonnen!")
elif Floor == Floris:
    print("Gelijkspel!")

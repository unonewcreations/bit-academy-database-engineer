import random

chips = 10
keuze = []
print(f"Je hebt {chips} chips!")

# num = random.randint(1, 36)

# voor testen
num = "1"

while chips > 0:
    vraag = input("Op welke nummers wil je inzetten? ")
    if vraag == "STOP":
        print("rien ne va plus")
        break
    elif vraag == " ":
        print("Geen juiste invoer!")
    elif int(vraag) <= 36 and int(vraag) >= 0:
        chips -= 1
        keuze.append(vraag)

    if chips == 0:
        print("rien ne va plus")
        print("GAME OVER")

for i in keuze:
    if i == num:
        print(f"De uitkomst is {i}")
        chips += 35
        print(f"Je hebt {chips} chips!")
    else:
        continue

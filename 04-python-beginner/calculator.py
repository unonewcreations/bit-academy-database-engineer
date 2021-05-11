import sys
# vragen operatie
# operatie = input("Welke operatie wil je uitvoeren, (+, -, *, /, of %)?\n")
operatie = input("Operatie? (+, -, *, /, of %)\n")

# gebruik membership operator
# if operatie not in "+-*/%":
#     print(operatie, "is geen geldige operatie")
#     sys.exit()
if operatie not in "+-*/%":
    print(operatie, "is geen geldige operatie")
    sys.exit()

# try:
#     # vragen eerste getal
#     getal1 = float(input("Eerste getal? "))
# except ValueError():
#     sys.exit("Kan", getal1, "niet omzetten naar een getal")
# # vragen tweede getal
# try:
#     getal2 = float(input("Tweede getal? "))
# except ValueError():
#     sys.exit(
#         "Kan", getal2, "niet omzetten naar een getal")
getal1 = input("Eerste getal?\n")
try:
    getal1 = float(getal1)
except ValueError:
    print("Kan", getal1, "niet omzetten naar een getal")
    sys.exit()
getal2 = input("Tweede getal?\n")
try:
    getal2 = float(getal2)
except ValueError:
    print("Kan", getal2, "niet omzetten naar een getal")
    sys.exit()


# operatie aftrekken
if operatie == "-":
    print("Resultaat: " + str(getal1-getal2))
# operatie optellen
elif operatie == "+":
    print("Resultaat: " + str(getal1+getal2))
# operatie vermenigvuldigen
elif operatie == "*":
    print("Resultaat: " + str(getal1*getal2))
# operatie delen
elif operatie == "/":
    if getal2 == 0:
        print("Kan niet delen door 0")
    else:
        print("Resultaat: " + str(getal1/getal2))
# operatie modulo
elif operatie == "%":
    if getal2 == 0:
        print("Kan niet delen door 0")
    else:
        print("Resultaat: " + str(getal1 % getal2))
# else:
#     print("Je hebt geen geldig operatie ingevuld")

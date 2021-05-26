import random
# start van spel 10 chips
chips = 10
inzet = []
while True:
    # check hoeveel chips de speler heeft
    if chips == 0:
        print("GAME OVER")
        break
    # print het aantal chips
    print(f"Je hebt {chips} chips!")
    # roulette input van de console
    num = input("Op welke nummers wil je inzetten?")
    # checken of input een cijfer is met functie isdigit()
    if num.isdigit():
        # num in de lijst toevoegen en chips in mindering brengen
        inzet.append(num)
        chips -= 1
    print(inzet)
    # Spel gaat beginnen, logica van het spel
    # rouletteChips == 0, betekent dat het spel gaat beginnen als speler al zijn beschikbare chips heeft ingezet.
    if chips == 0 or num == "STOP":
        print("rien ne va plus")
        # balletje is gevallen op routeletteUitkomst
        uitkomst = random.randint(1, 36)
        print(f"De uitkomst is {uitkomst}")
        # checken van rouletteInzet tov routeletteUitkomst
        #rouletteInzet = ['1', '2', '3', '4']
        for inzet in num:
            # controleren en verwerken van uitkomst en chips aantal bijwerken
            if int(inzet) == uitkomst:
                print("Correct gegokt!!! +35")
                # winst (35) + ingezette chip (1)
                chips += 36
            else:
                print("Fout gegokt")
        # reset (maak lijst leeg) rouletteInzet voor nieuwe ronde
        inzet = []
    if num == "BREAK":
        # Spel afsluiten
        print("Doei")
        break

score1 = int(input("Wat is score speler 1? "))
print(score1)
score2 = int(input("Wat is score speler 2? "))
print(score2)

if score1 > score2:
    print("Speler 1 heeft gewonnen")
elif score1 < score2:
    print("Speler 2 heeft gewonnen")
elif score1 == score2:
    print("Speler 1 en Speler 2 hebben gelijk gespeeld!")

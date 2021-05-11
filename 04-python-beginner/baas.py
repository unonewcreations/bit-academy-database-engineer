# Het wachtwoord wat de gebruiker invoert wordt vergeleken met het correcte wachtwoord.
# De uitkomst van de vergelijking wordt opgeslagen in een variable, of direct weergegeven in de terminal.
# Wanneer de gebruiker het goede wachtwoord invoert staat er `Baas ingelogd: True`. Anders staat er `Baas ingelogd: False`.
print("Wat is het wachtwoord?")
a = input()
w = a
if w == "baas":
    print("Baas ingelogd: True")
else:
    print("Baas ingelogd: False")

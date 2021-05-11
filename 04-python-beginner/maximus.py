# Lijst met getallen
num = [3, 7, 10, 40, 2, 4, 8]
# Begin variabele
max_value = None
# Doorloop lijst. i is output getallen in lijst
for i in num:
    # doorloop lijst voor hoogste getal
    if (max_value is None or i > max_value):
        max_value = i
# Print hoogste getal
print(max_value)

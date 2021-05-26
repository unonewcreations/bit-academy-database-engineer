import datetime

j = int(input('Wat is het jaar?\n'))
m = int(input('Wat is het maandnummer?\n'))
d = int(input('Wat is de dag?\n'))

i_date = datetime.datetime(j, m, d)
# print(i_date)20

t_date = datetime.datetime.today()
# print(t_date)

delta = t_date - i_date
print(delta)

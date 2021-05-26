# kopieer dictionary
bezittingen = {
    'goud': 500,
    'buidel': ['touw', 'vuursteen', 'zakmes'],
    'rugzak': ['panfluit', 'dolk', 'slaapzak', 'appel']
}

# toevoegen key zilver
# syntax = dict[key] = value
bezittingen['zilver'] = 12

# verwijderen zakmes
#synyax = dict[key].function(value)
bezittingen['buidel'].remove('zakmes')

# ordenen items rugzak
rugzak = bezittingen['rugzak']
rugzak.sort()

print(bezittingen)

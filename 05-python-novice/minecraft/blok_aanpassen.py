# import module to work with json
import json

# open json file
with open('gras_blok.json') as f:
    data = json.load(f)

# change data
data['block']['snow'] = True
data['block']['coordinates']['y'] += 66
data['block']['coordinates']['z'] *= 3

# export changed data to json file
with open('sneeuw_blok.json', 'w') as outfile:
    json.dump(data, outfile)

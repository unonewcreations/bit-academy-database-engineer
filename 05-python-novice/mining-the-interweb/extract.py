# import packages
import sys
import requests


# get argument from command line
arg = int(sys.argv[1])

# get data from html
get_data = requests.get('https://jsonplaceholder.typicode.com/todos')

# put data in variable
put_data = get_data.json()

# number between 1 and 200
if arg in range(1, 200):
    # print title from list
    print(put_data[arg]["title"])
# print number if not between 1 and 200
else:
    print('Geef een nummer op tussen 1 en 200')

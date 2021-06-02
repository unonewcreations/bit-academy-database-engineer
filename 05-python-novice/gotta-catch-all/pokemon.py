# import packages
import mysql.connector
import requests


# connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# point to database
conn = mydb.cursor()

# create the database if it doesn't exist.
conn.execute("CREATE DATABASE IF NOT EXISTS pokemon")

# create the table if it doesn't exist.
conn.execute(
    "CREATE TABLE IF NOT EXISTS users (id int, name varchar(255), weight int, height int)")
exit()

# get argument from command line
# arg = int(sys.argv[1])

# get data from html
get_data = requests.get('https://pokeapi.co/api/v2/pokemon/')

# put data in variable
put_data = get_data.json()
print(put_data)

# # number between 1 and 200
# if arg in range(1, 200):
#     # print title from list
#     print(put_data[arg]["title"])
# # print number if not between 1 and 200
# else:
#     print('Geef een nummer op tussen 1 en 200')

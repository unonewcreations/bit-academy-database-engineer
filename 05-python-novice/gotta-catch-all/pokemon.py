# import packages
import json
import mysql.connector
import requests


# connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pokemon"
)

# point to database
conn = mydb.cursor()

# create the database if it doesn't exist.
conn.execute("CREATE DATABASE IF NOT EXISTS pokemon")

# create the table if it doesn't exist.
conn.execute(
    "CREATE TABLE IF NOT EXISTS pokemon_data (id int, name varchar(255), weight int, height int)")

# get data from html and create list
pok_tabel = []
for x in range(1, 151):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(x))
    pok_data = response.json()
    pok_tabel.append(pok_data)

# Insert each entry from json into the table.
pok_car = ['id', 'name', 'weight', 'height']
for entry in pok_tabel:

    # this will make sure that each key will default to None
    # if the key doesn't exist in the json entry.
    values = [entry.get(key, None) for key in pok_car]

    # execute the command and replace '?' with the each value
    # in 'values'.
    cmd = "INSERT INTO pokemon_data VALUES(%s, %s, %s, %s)"
    conn.execute(cmd, values)
mydb.commit()
mydb.close

# print messsage
print('Succes! Alle pokemons zijn gevangen')

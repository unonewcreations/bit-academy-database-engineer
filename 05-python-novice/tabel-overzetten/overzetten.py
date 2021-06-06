# import required module
import json
import mysql.connector


# connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="overzetten"
)

# point to database
conn = mydb.cursor()

# create the database if it doesn't exist.
# conn.execute("CREATE DATABASE IF NOT EXISTS overzetten")

# create the table if it doesn't exist.
conn.execute(
    "CREATE TABLE IF NOT EXISTS users (name varchar(255), gender varchar(255), age int, fav_color varchar(255))")

# open json file
f = open("gebruikers.json")

# returns json object as a dictionary
data = json.load(f)

# Insert each entry from json into the table.
keys = ["name", "gender", "age", "fav_color"]
for entry in data:

    # This will make sure that each key will default to None
    # if the key doesn't exist in the json entry.
    values = [entry.get(key, None) for key in keys]

    # Execute the command and replace '?' with the each value
    # in 'values'.
    cmd = "INSERT INTO users VALUES(%s, %s, %s, %s)"
    conn.execute(cmd, values)
mydb.commit()
mydb.close()

print("Geslaagd!")

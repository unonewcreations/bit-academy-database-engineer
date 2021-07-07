# install libraries
import csv
import mysql.connector

# connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# create a cursor object using the cursor() method
mycursor = mydb.cursor()

# create sql database if not existing
mycursor.execute("CREATE DATABASE IF NOT EXISTS marathon")
mycursor.execute("USE marathon")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS results (year INT, winner VARCHAR(255), gender VARCHAR(255), country VARCHAR(255), time TIME, marathon VARCHAR(255))")
mycursor.execute("DELETE FROM results")

# read the csv file from current directory
file = open('marathon_results.csv')
csv_data = csv.reader(file)

# iterate the file and skip the header
skipHeader = True
print("CSV-bestand in de MySQL-database aan het laden...")
for row in csv_data:
    if skipHeader:
        skipHeader = False
        continue
    mycursor.execute(
        'INSERT INTO results(year, winner, gender, country, time, marathon)''VALUES(%s, %s, %s, %s, %s, %s)', row)
print("Bestand succesvol geladen!")
mydb.commit()
mydb.close()

import csv
import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marathon"
)

mycursor = mydb.cursor()

if len(sys.argv) > 1:
    arg = sys.argv[1]
    file = open('2017.csv')
    csv_data = csv.reader(file)

    skipHeader = True
    print("CSV-bestand in de MySQL-database aan het laden...")
    for row in csv_data:
        if skipHeader:
            skipHeader = False
            continue
        mycursor.execute(
            'INSERT INTO results(year, winner, gender, country, time, marathon)''VALUES(%s, %s, %s, %s, %s, %s)', row)
    print("Bestand succesvol geladen!")
else:
    print("Error: geen bestand geleverd!")

mydb.commit()
mydb.close()

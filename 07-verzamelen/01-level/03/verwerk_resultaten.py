import csv
import sys
import mysql.connector
import os
import glob
import pandas as pd

path = "C:/Users/akron/CloudStation\Website/Unonew/Learn\Bit-academy/07-verzamelen/01-03_van-archief-naar-database/archive"

all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f, sep=',')
                     for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged = df_merged.iloc[:, :-1]
print(df_merged)
df_merged.to_csv("merged.csv", index=False)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marathon"
)

mycursor = mydb.cursor()

if len(sys.argv) > 1:
    arg = sys.argv[1]
    file = open("merged.csv")
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

mycursor.close()
mydb.commit()
mydb.close()

# install libraries
import mysql.connector
import pandas as pd

# get csv file
data = pd.read_csv('marathon_results.csv')
df = pd.DataFrame(data=data)
print(df)

# connect to MySQL and create database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE IF NOT EXISTS marathon")

# mycursor.execute("CREATE TABLE IF NOT EXISTS marathon_results)

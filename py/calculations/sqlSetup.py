import sqlite3 as sql

setupDb = sql.connect('machineDatabase.db')

cursor = setupDb.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (Title TEXT, Director TEXT, Year INT)''')
              
setupDb.commit
setupDb.close
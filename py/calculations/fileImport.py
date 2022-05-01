import sqlite3 as sql
import os
import os.path
from config.definitions import (
    ROOT_DIR,
    climbDirectory
)

def saveMachine (Machine_Name, Completion_Time):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(2)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('machineDatabase.db')
    cursor = setupDb.cursor()
    
    #sql statement
    sql1 = '''INSERT INTO Machines (Machine_Name, Completion_Time)
        VALUES
            (?, ?)''',
            (Ma
            
    sql2 = '''CREATE TABLE IF NOT EXISTS Machines
                  (Machine_Name TEXT, Completion_Time TEXT)'''

    #Creates table if not created, otherwise will return machine name and time left
    cursor.execute(sql2)
    cursor.execute(sql1)            
    setupDb.commit
    
    cursor.execute("SELECT * FROM Machines")
    print(cursor.fetchall())
    
    setupDb.close

saveMachine("Tsugami 5", "3/15/2022")
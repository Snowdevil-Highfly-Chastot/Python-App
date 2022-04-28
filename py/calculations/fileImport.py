import sqlite3 as sql
import os
import os.path

def readMachineDatabase (machine):

    #Gets current working directory
    currentPath = os.getcwd()
    
    #Changes current directory to db directory and sets to active
    os.chdir(currentPath + '\\db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('machineDatabase.db')
    cursor = setupDb.cursor()
    
    #Creates table if not created, otherwise will return machine name and time left
    cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                  (Machine_Name TEXT, Time_left DATE)''')             
    setupDb.commit
    setupDb.close

readMachineDatabase("Tsugami 5")
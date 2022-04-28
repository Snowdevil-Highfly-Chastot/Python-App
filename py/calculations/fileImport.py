import sqlite3 as sql
import os
import os.path

def readMachineDatabase (machine):

    #Gets current working directory
    currentPath = os.getcwd()
    
    #Sets grandparent directory to active directory
    os.chdir(currentPath + '\\db')
    
    # Gets all directories in the folder as a tuple
    o = [os.path.join(currentPath,o) for o in os.listdir(currentPath) if os.path.isdir(os.path.join(currentPath,o))]

    setupDb = sql.connect('machineDatabase.db')
    cursor = setupDb.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                  (Title TEXT, Director TEXT, Year INT)''')
                  
    setupDb.commit
    setupDb.close

readMachineDatabase("Tsugami 5")
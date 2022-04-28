import sqlite3 as sql
import os
import os.path

def readMachineDatabase (machine):
    #Reads CSV machine database to pull completion time

    #Gets current working directory
    currentPath = os.getcwd()
    
    #Selects parent directory
    pathParent = os.path.dirname(currentPath)
    
    #Selects grandparent directory
    pathGrandparent = os.path.dirname(pathParent)
    
    #Sets grandparent directory to active directory
    os.chdir(pathGrandparent)
    
    # Gets all directories in the folder as a tuple
    o = [os.path.join(pathGrandparent,o) for o in os.listdir(pathGrandparent) if os.path.isdir(os.path.join(pathGrandparent,o))]
    
    print(o)
    
    #Combs data for the csv file
    for item in o:
        if os.path.exists(item + 'db/):
            pickedFile = item + 'db/'

    setupDb = sql.connect('machineDatabase.db')
    
    cursor = setupDb.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                  (Title TEXT, Director TEXT, Year INT)''')
                  
    setupDb.commit
    setupDb.close

readMachineDatabase("Tsugami")
import sqlite3 as sql
import os
import os.path
from .config.configLibrary import (
    ROOT_DIR,
    climbDirectory
)

def readMachines(Column):

    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)

    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('appDatabase.db', detect_types=sql.PARSE_DECLTYPES)
    setupDb.text_factory = str
    cursor = setupDb.cursor()

    #Assigns the query to a variable
    query = cursor.execute('''SELECT Machine_Name FROM Machines''')

    #Turns the queried information into a Python list to access individual cell items easier
    item = query.fetchall()

    #Sets the result as the individual item queried using the inputted column paramter
    result = item[Column][0]

    #Closes db and returns the desired cell item
    setupDb.close
    return str(result)


import sqlite3 as sql
import os
import os.path
from config.definitions import ROOT_DIR

def saveMachine ():
    
    databasePath = os.path.join(ROOT_DIR, 'db')
    print(databasePath)
    
    #Changes current directory to db directory and sets to active
    os.chdir(databasePath)

    cwd = os.getcwd()
    print(cwd)

    # #Creates database if not created, otherwise connects to it
    # setupDb = sql.connect('machineDatabase.db')
    # cursor = setupDb.cursor()
    
    # #sql statement
    # sql1 = ''' INSERT INTO Machines(machine_name,completion_time)
    #         VALUES(?,?)'''
    # sql2 = '''CREATE TABLE IF NOT EXISTS Machines
    #               (Machine_Name TEXT, Completion_Time TEXT)'''

    # #Creates table if not created, otherwise will return machine name and time left
    # cursor.execute(sql2)
    # cursor.execute(sql1)             
    # setupDb.commit
    # setupDb.close

saveMachine()
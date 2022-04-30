import sqlite3 as sql
import os
import os.path
from config.definitions import ROOT_DIR

def saveMachine (machine, time):
    
    print(os.path.join(ROOT_DIR, 'py', 'testing', 'test.py'))

    #Gets current working directory
    currentPath = os.getcwd()
    
    #Changes current directory to db directory and sets to active
    os.chdir('..')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('machineDatabase.db')
    cursor = setupDb.cursor()
    
    #sql statement
    sql1 = ''' INSERT INTO Machines(machine_name,completion_time)
            VALUES(?,?)'''
    sql2 = '''CREATE TABLE IF NOT EXISTS Machines
                  (Machine_Name TEXT, Completion_Time TEXT)'''

    #Creates table if not created, otherwise will return machine name and time left
    cursor.execute(sql2)
    cursor.execute(sql1)             
    setupDb.commit
    setupDb.close

saveMachine("Tsugami 5", "asd")
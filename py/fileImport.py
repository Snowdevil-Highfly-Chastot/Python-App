import sqlite3 as sql
import os
import os.path
from .config.definitions import (
    ROOT_DIR,
    climbDirectory
)

def saveMachine (Machine_Name, Completion_Time):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('machineDatabase.db')
    cursor = setupDb.cursor()

    #Creates table if not created, otherwise will return machine name and time left
    cursor.execute('''CREATE TABLE IF NOT EXISTS Machines
    (Machine_Name TEXT, Completion_Time TIMESTAMP)''')
    
    cursor.execute('''DELETE FROM Machines WHERE Machine_Name = '%s' ''' % Machine_Name)
    
    cursor.execute('''INSERT INTO Machines (Machine_Name, Completion_Time) 
    VALUES (?, ?)''', (Machine_Name, Completion_Time))
     
    setupDb.commit()
    print("Post Complete")
    setupDb.close

def readMachine (Machine_Name):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('machineDatabase.db')
    cursor = setupDb.cursor()
    
    cursor.execute('''SELECT * FROM Machines WHERE Machine_Name = '%s' ''' % Machine_Name)
    
    rows = cursor.fetchall()
    for row in rows:
        print(rows)
    setupDb.close
    
    
def saveJob(Part_Name, Part_Desc, Machine_Name, Time_Per_Part, Completion_Time, Oal,Cut_Off_Width, Bar_Length, Bar_Parameter, Active):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('appDatabase.db')
    cursor = setupDb.cursor()

    #Creates table if not created, otherwise will return machine name and time left
    cursor.execute('''CREATE TABLE IF NOT EXISTS Jobs
    (Part_Name TEXT, Part_Desc TEXT, Machine_Name TEXT, Time_Per_Part INT, Completion_Time TIMESTAMP, Oal INT, Cut_Off_Width INT, Bar_Length INT, Bar_Parameter INT, Active TEXT)''')
    
    cursor.execute('''DELETE FROM Jobs WHERE Part_Name = '%s' OR Machine_Name = '%s' ''' % (Part_Name, Machine_Name))
    
    cursor.execute('''INSERT INTO Jobs (Part_Name, Part_Desc, Machine_Name, Time_Per_Part, Completion_Time, Oal,Cut_Off_Width, Bar_Length, Bar_Parameter, Active) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (Part_Name, Part_Desc, Machine_Name, Time_Per_Part, Completion_Time, Oal,Cut_Off_Width, Bar_Length, Bar_Parameter, Active))
     
    setupDb.commit()
    setupDb.close

def readJob(Column, Part_Name, Machine_Name, Active):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('appDatabase.db')
    cursor = setupDb.cursor()
    
    result = cursor.execute('''SELECT * FROM Jobs WHERE Part_Name = '%s' AND Machine_Name = '%s' AND Active = '%s' ''' % (Part_Name, Machine_Name, Active)).fetchone()[Column]
    
    return result
    
    setupDb.close
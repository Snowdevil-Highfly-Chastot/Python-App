import sqlite3 as sql
import os
import os.path
from .config.configLibrary import (
    ROOT_DIR,
    climbDirectory
)
from .classLibrary import completionTime

def saveMachine (Machine_Name, Description, Machine_Type, Location):
    
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
    cursor.execute('''CREATE TABLE IF NOT EXISTS Machines
    (Machine_Name TEXT, Description TEXT, Machine_Type TEXT, Location TEXT)''')
    
    cursor.execute('''DELETE FROM Machines WHERE Machine_Name = '%s' ''' % Machine_Name)
    
    cursor.execute('''INSERT INTO Machines (Machine_Name, Description, Machine_Type, Location) 
    VALUES (?, ?, ?, ?)''', (Machine_Name, Description, Machine_Type, Location))
     
    setupDb.commit()
    setupDb.close

def readMachine (Column, Machine_Name):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('appDatabase.db', detect_types=sql.PARSE_DECLTYPES)
    cursor = setupDb.cursor()
    
    #Assigns the query to a variable
    query = cursor.execute('''SELECT * FROM Machines WHERE Machine_Name = '%s' ''' % Machine_Name)
    
    #Turns the queried information into a Python list to access individual cell items easier
    item = list(query.fetchone())

    #Sets the result as the individual item queried using the inputted column paramter
    result = item[Column]
    
    #Closes db and returns the desired cell item
    setupDb.close
    return result
    
def deleteMachine (Machine_Name):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('appDatabase.db')
    cursor = setupDb.cursor()
    
    #Deletes machines with the selected machine name
    cursor.execute('''DELETE FROM Machines WHERE Machine_Name = '%s' ''' % (Machine_Name))
    
    #Commits and closes the database
    setupDb.commit()
    setupDb.close
    
    
def saveJob(Part_Name, Part_Desc, Machine_Name, Parts_Needed, Time_Per_Part, Oal,Cut_Off_Width, Bar_Length, Bar_Parameter, Active):
    
    #Tries to calculate the completion time for db entry, otherwise returns string if cannot calculate
    try:
        Completion_Time = completionTime(int(Parts_Needed), int(Time_Per_Part))
    except:
        Completion_Time = "No time or count entered"
    
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
    (Part_Name TEXT, Part_Desc TEXT, Machine_Name TEXT, Parts_Needed INT, Time_Per_Part INT, Completion_Time TEXT, Oal INT, Cut_Off_Width INT, Bar_Length INT, Bar_Parameter INT, Active TEXT)''')
    
    #Deletes the existing job row to avoid overpopulating db with unused entries
    cursor.execute('''DELETE FROM Jobs WHERE Part_Name = '%s' OR Machine_Name = '%s' ''' % (Part_Name, Machine_Name))
    
    #Adds the new row with the updated information
    cursor.execute('''INSERT INTO Jobs (Part_Name, Part_Desc, Machine_Name, Parts_Needed, Time_Per_Part, Completion_Time, Oal,Cut_Off_Width, Bar_Length, Bar_Parameter, Active) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (Part_Name, Part_Desc, Machine_Name, Parts_Needed, Time_Per_Part, Completion_Time, Oal,Cut_Off_Width, Bar_Length, Bar_Parameter, Active))
     
    #Commits and closes the database
    setupDb.commit()
    setupDb.close

def readJob(Column, Machine_Name):
    
    #Find current path of this folder
    currentPath = os.path.join(ROOT_DIR)
    
    #Changes current directory to db directory in relation to this file
    os.chdir(currentPath)
    climbDirectory(1)
    os.chdir('db')

    #Creates database if not created, otherwise connects to it
    setupDb = sql.connect('appDatabase.db', detect_types=sql.PARSE_DECLTYPES)
    cursor = setupDb.cursor()
    
    #Assigns the query to a variable
    query = cursor.execute('''SELECT * FROM Jobs WHERE Machine_Name = '%s' ''' % Machine_Name)
    
    #Turns the queried information into a Python list to access individual cell items easier
    item = list(query.fetchone())

    #Sets the result as the individual item queried using the inputted column paramter
    result = item[Column]
    
    #Closes db and returns the desired cell item
    setupDb.close
    return result
    
    
import csv
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
    
    #Combs data for the csv file
    for item in o:
        if os.path.exists(item + '/machineDatabase.csv'):
            pickedFile = item + '/machineDatabase.csv'
            
    #Opens file as CSV
    file = open(pickedFile, "r")
    csvreader = csv.reader(file)

    #Pulls data and separates headers from rows
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if row[0] == machine:
            rows.append(row)
    print(rows[0][1])

    #Closes file after use, needed anytime any file is opened
    file.close()
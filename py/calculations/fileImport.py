import csv
import os
import os.path

def readMachineDatabase ():
    #Reads CSV machine database to pull completion time

    #Gets current working directory
    currentPath = os.getcwd()
    
    #Selects parent directory
    pathParent = os.path.dirname(currentPath)
    print(pathParent)
    
    #Selects grandparent directory
    pathGrandparent = os.path.dirname(pathParent)
    print(pathGrandparent)
    
    #Sets grandparent directory to active directory
    os.chdir(pathGrandparent)
    
    # Gets all directories in the folder as a tuple
    o = [os.path.join(pathGrandparent,o) for o in os.listdir(pathGrandparent) if os.path.isdir(os.path.join(pathGrandparent,o))]
    print(o)
    

    #Combs data for the csv file
    for item in o:
        if os.path.exists(item + '/machineDatabase.csv'):
            pickedFile = item + '/machineDatabase.csv'
        else:
            print("none")
            

    #Opens file as CSV
    file = open(pickedFile, "r")
    csvreader = csv.reader(file)

    #Pulls data and separates headers from rows
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)

    #if rows == machine:
        #print(rows)



    #Closes file after use, needed anytime any file is opened
    file.close()

readMachineDatabase()
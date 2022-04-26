import csv
import os
import os.path

def readMachineDatabase (machine):
    #Reads CSV machine database to pull completion time

    d = os.getcwd() #Gets the current working directory
    os.chdir("..") #Go up one directory from working directory
    o = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))] # Gets all directories in the folder as a tuple

    #Combs data for the csv file
    for item in o:
        if os.path.exists(item + '\\machineDatabase.csv'):
            pickedFile = item + '\\machineDatabase.csv'

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

    if rows == machine:
        print(rows)



    #Closes file after use, needed anytime any file is opened
    file.close()

readMachineDatabase("Tsugami 5")
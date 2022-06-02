import datetime
from .machineClassLibrary import (
runTimeLeft,
completionTime,
partsRemaining,
timeRemaining,
barfeedParts
)

from .fileImport import (
saveMachine,
readMachine,
saveJob,
readJob
)

#Creates Machine class for handling all of the machines
class Machine:
    def __init__(self, machineName, desc, machineType, location):
        
        self.machineName = machineName
        self.desc = desc
        self.machineType = machineType
        self.location = location

    def postMachine(self):
        
        #Saves the classes information into the database
        saveMachine(self.machineName, self.desc, self.machineType, self.location)
        
    def grabMachine(self, Column):

        #Returns a single item by using the machine name to get the row, and the column parameter
        result = readMachine(Column, self.machineName)
        return result

        
#Creates the job class for handling all machine jobs
class Job:
    def __init__ (self, Machine_Name, Part_Name = "", Part_Desc = "", Time_Per_Part = 0, 
    Parts_Needed = 0, Oal = 0, Cut_Off_Width = 0, Bar_Length = 0, Bar_Parameter = 0, Active = "y"):
     
        self.Machine_Name = Machine_Name
        self.Part_Name = Part_Name
        self.Part_Desc = Part_Desc
        self.Parts_Needed = Parts_Needed
        self.Time_Per_Part = Time_Per_Part
        self.Oal = Oal
        self.Cut_Off_Width = Cut_Off_Width
        self.Bar_Length = Bar_Length
        self.Bar_Parameter = Bar_Parameter
        self.Active = Active
        
    def postJob(self):
        
        #Saves the classes information into the database
        saveJob(self.Part_Name, self.Part_Desc, self.Machine_Name, self.Parts_Needed, self.Time_Per_Part, self.Oal,self.Cut_Off_Width, self.Bar_Length, self.Bar_Parameter, self.Active)
        
    def grabJob(self, Column):

        #Returns a single item by using the machine name to get the row, and the column parameter
        result = readJob(Column, self.Machine_Name)
        return result

    def jobFinished(self):
        
        #Calculates how many D:H:M:S are left in a job
        result = runTimeLeft(self.Parts_Needed, self.Time_Per_Part)
        return result
        
    def partsLeft(self):
    
        #Calculates amount of parts left on run by using the completion time in database
        completionTimeString = readJob(5, self.Machine_Name)
        completionTimeDateFormat = datetime.datetime.strptime(completionTimeString, '%Y-%m-%d %H:%M:%S')
        result = partsRemaining(completionTimeDateFormat, self.Time_Per_Part)
        return result
        
    def timeLeft(self):
        
        #Calculates total time left down to tge second
        completionTimeString = readJob(5, self.Machine_Name)
        completionTimeDateFormat = datetime.datetime.strptime(completionTimeString, '%Y-%m-%d %H:%M:%S')
        result = timeRemaining(completionTimeDateFormat)
        return result
        
    # def barfeedParts(self):
        
    #     totalParts = barfeedParts(self.partLength, self.cutoffWidth, self.barfeedParameter, self.barLength)
        
    #     print(totalParts, "Parts Per Bar")
    #     return totalParts
        
    # def barfeedCompletionTime(self):
    
    #     totalParts = barfeedParts(self.partLength, self.cutoffWidth, self.barfeedParameter, self.barLength)
    
    #     #Set variables and calculate timing
    #     totalTime = self.partTime * totalParts
    #     now = datetime.datetime.now()
    #     timeCompleted = now + datetime.timedelta(seconds = totalTime)
        
    #     print(timeCompleted, "End of bar")
    #     return timeCompleted
        
    # def barfeedTime(self):
    
    #     totalParts = barfeedParts(self.partLength, self.cutoffWidth, self.barfeedParameter, self.barLength)
    #     runTimeLeft(totalParts, self.partTime)
        

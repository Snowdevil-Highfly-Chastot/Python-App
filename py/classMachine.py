import datetime
from .machineClassLibrary import (
runTimeLeft,
completionTime,
barfeedParts
)

from .fileImport import (
saveMachine,
readMachine,
saveJob,
readJob
)

class machine:
    def __init__(self, name, partsNeeded = 0, partTime = 0, partLength = 0, barLength = 0, cutoffWidth = 0, barfeedParameter = 0):
        
        self.name = name
        self.partTime = partTime
        self.partsNeeded = partsNeeded
        self.partLength = partLength
        self.barLength = barLength
        self.cutoffWidth = cutoffWidth
        self.barfeedParameter = barfeedParameter
    
    def jobFinished(self):
        
        print("Calculating...")
        runTimeLeft(self.partsNeeded, self.partTime)
        
    def postCompletionTime(self):
        
        print("posting...")
        saveMachine(self.name, completionTime(self.partTime, self.partsNeeded))

    def pullCompletionTime(self):

        print("fetching...")
        readMachine(self.name)
        
    def barfeedParts(self):
        
        totalParts = barfeedParts(self.partLength, self.cutoffWidth, self.barfeedParameter, self.barLength)
        
        print(totalParts, "Parts Per Bar")
        return totalParts
        
    def barfeedCompletionTime(self):
    
        totalParts = barfeedParts(self.partLength, self.cutoffWidth, self.barfeedParameter, self.barLength)
    
#Set variables and calculate timing
        totalTime = self.partTime * totalParts
        now = datetime.datetime.now()
        timeCompleted = now + datetime.timedelta(seconds = totalTime)
        
        print(timeCompleted, "End of bar")
        return timeCompleted
        
    def barfeedTime(self):
    
        totalParts = barfeedParts(self.partLength, self.cutoffWidth, self.barfeedParameter, self.barLength)
        runTimeLeft(totalParts, self.partTime)
        
class Job:
    def __init__ (self, Machine_Name, Part_Name, Part_Desc = "", Time_Per_Part = 0, Completion_Time = "", Oal = 0, Cut_Off_Width = 0, Bar_Length = 0, Bar_Parameter = 0, Active = "y"):
     
        self.Machine_Name = Machine_Name
        self.Part_Name = Part_Name
        self.Part_Desc = Part_Desc
        self.Time_Per_Part = Time_Per_Part
        self.Completion_Time = Completion_Time
        self.Oal = Oal
        self.Cut_Off_Width = Cut_Off_Width
        self.Bar_Length = Bar_Length
        self.Bar_Parameter = Bar_Parameter
        self.Active = Active
        
    def postJob(self):
        
        print("Posting...")
        saveJob(self.Part_Name, self.Part_Desc, self.Machine_Name, self.Time_Per_Part, self.Completion_Time, self.Oal,self.Cut_Off_Width, self.Bar_Length, self.Bar_Parameter, self.Active)
        print("Posted!")
        
    def grabJob(self, Column):
        print("Reading...")
        result = readJob(Column, self.Part_Name, self.Machine_Name, self.Active)
        print(result)

       
#Initializing Class below for testing
#job1 = Job("Tsugami 8", "404-44-1", "Diffuser from the 404 family", 70,"Tomorrow",2.25,.095,144,5.2,"y")
#job1.postJob()
#job1.grabJob(2)
#print("")
        
#machine1 = machine("Tsugami 5", 1200, 117, 2.625, 144, 0.95, 3.5)
#machine1.postCompletionTime()
#machine1.barfeedParts()
#machine1.barfeedCompletionTime()
#machine1.barfeedTime()
#machine1.pullCompletionTime()
#print(" ")

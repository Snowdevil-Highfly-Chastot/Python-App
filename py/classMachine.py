import datetime
from machineClassLibrary import (
runTimeLeft,
completionTime,
barfeedParts
)

from fileImport import (
saveMachine,
readMachine
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
 
       
#Initializing Class below for testing
        
machine1 = machine("Tsugami 5", 1200, 117, 2.625, 144, 0.95, 3.5)
#machine1.postCompletionTime()
machine1.barfeedParts()
machine1.barfeedCompletionTime()
machine1.barfeedTime()
machine1.pullCompletionTime()
print(" ")

machine2 = machine("Tsugami 6", 4000, 109)
#machine2.postCompletionTime()
machine2.pullCompletionTime()
print(" ")

machine3 = machine("Tsugami 7", 1000, 59)
#machine3.postCompletionTime()
machine3.pullCompletionTime()
print(" ")

machine4 = machine("Tsugami 8", 6000, 42)
#machine4.postCompletionTime()
machine4.pullCompletionTime()
print(" ")
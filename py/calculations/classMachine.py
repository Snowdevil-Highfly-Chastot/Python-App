from functionRunTimeLeft import runTimeLeft
from fileImport import (
saveMachine,
readMachine
)

class machine:
    def __init__(self, name, partTime, partsNeeded):
        self.name = name
        self.partTime = partTime
        self.partsNeeded = partsNeeded
    
    def jobFinished(self):
        
        print(self.name)
        runTimeLeft(self.partTime, self.partsNeeded)
        
    def postCompletionTime(self):
    	
    	print("posting...")
    	saveMachine(self.name, runTimeLeft(self.partTime, self.partsNeeded))
    	

    def pullCompletionTime(self):

        print("fetching...")
        readMachine(self.name)
        
        
machine1 = machine("Tsugami 5", 117, 950)
#machine1.postCompletionTime()
machine1.pullCompletionTime()
print(" ")

machine2 = machine("Tsugami 6", 12, 50)
#machine2.postCompletionTime()
machine2.pullCompletionTime()
print(" ")

machine3 = machine("Tsugami 7", 55, 2400)
#machine3.postCompletionTime()
machine3.pullCompletionTime()
print(" ")

machine4 = machine("Tsugami 8", 65, 1400)
#machine4.postCompletionTime()
machine4.pullCompletionTime()
print(" ")
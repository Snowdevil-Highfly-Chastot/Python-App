from functionRunTimeLeft import runTimeLeft

class machine:
    def __init__(self, name, partTime, partsNeeded):
        self.name = name
        self.partTime = partTime
        self.partsNeeded = partsNeeded
    
    def jobFinished(self):
        
        print(self.name)
        runTimeLeft(self.partTime, self.partsNeeded)
        print(" ")
        
        
machine1 = machine("Tsugami 5", 117, 950)
machine1.jobFinished()
machine2 = machine("Tsugami 6", 102, 3350)
machine2.jobFinished()
machine3 = machine("Tsugami 7", 55, 2400)
machine3.jobFinished()
machine4 = machine("Tsugami 8", 65, 1400)
machine4.jobFinished()
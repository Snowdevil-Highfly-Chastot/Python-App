import math
import datetime

#Calculates time from starting a new bar to the next bar change sequence
#Lengths are in inches
#Time is in seconds

def barTimeLeft(partLength, cutoffWidth, machineTime, barParameter):
    
    #Set variables and calculate parts needed to finish a bar
    actualPartLength = partLength + cutoffWidth
    actualBarLength = 144 - barParameter
    totalPartsUsed = math.floor(actualBarLength / actualPartLength)
    
    #Set variables and calculate timing
    totalTime = machineTime * totalPartsUsed
    now = datetime.datetime.now()
    timeCompleted = now + datetime.timedelta(seconds = totalTime)
    
    print(actualPartLength, "Actual Length")
    print(actualBarLength, "Actual bar length")
    print(totalPartsUsed, "Max parts made per bar")
    print(totalTime, "Total time in seconds till bar is done")
    print(now, "This is the current time")
    print(timeCompleted, "This is when the bar will be finished")
    

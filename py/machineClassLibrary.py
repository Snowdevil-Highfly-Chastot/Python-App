import math
import datetime

#Calculates time left on a job using the count and seconds per part
def runTimeLeft(partCount, partTime):
    
#Create blank dictionary
    totalTime = {}
    
#Function to cut down on repeat math
    def timeMath(seconds):

        if seconds == 0:
            return math.floor(int(partCount) * int(partTime))
        else:
            return math.floor(int(partCount) * int(partTime) / seconds)
    
#Math to convert total seconds to Days, Hours, Minutes, and Seconds.
    dayTimeLeft = timeMath(86400)
    hourTimeLeft = timeMath(3600) - (dayTimeLeft * 24)
    minuteTimeLeft = timeMath(60) - ((hourTimeLeft * 60) + (dayTimeLeft * 1440))
    secondTimeLeft = timeMath(0) - ((minuteTimeLeft * 60) + (hourTimeLeft * 3600) + (dayTimeLeft * 86400))

#Do not return variables with 0 and display separate time left values
    if dayTimeLeft > 0:
        totalTime.update({"Days" : dayTimeLeft})
    if hourTimeLeft > 0:
        totalTime.update({"Hours" : hourTimeLeft})
    if minuteTimeLeft > 0:
        totalTime.update({"Minutes" : minuteTimeLeft})
    if secondTimeLeft > 0:
        totalTime.update({"Seconds" : secondTimeLeft})
        
    return totalTime

#Calculates date and time for the job to be done running
def completionTime(partCount, partTime):
    
#Setting date/partTime variables to calculate finish date/partTime
    now = datetime.datetime.now()
    jobFinished = now + datetime.timedelta(seconds = partCount * partTime)

    return jobFinished
    
def partsRemaining(completionTime, secondsPerPart):
    #Gets current date and time
    now = datetime.datetime.now()
    
    #Calculates total seconds between now and the completion time
    totalSeconds = (completionTime - now).total_seconds()
    
    #Calculates approx. parts left from the total seconds and seconds to make each part
    currentPartCount = math.ceil(totalSeconds / secondsPerPart)
    
    return currentPartCount
    

#Calculates amount of parts possible to machine per bar	
def barfeedParts(partLength, cutoffWidth, barfeedParameter, barLength):
    
#Set variables and calculate parts needed to finish a bar
    actualPartLength = partLength + cutoffWidth
    actualBarLength = barLength - barfeedParameter
    totalParts = math.floor(actualBarLength / actualPartLength)

    return totalParts
    
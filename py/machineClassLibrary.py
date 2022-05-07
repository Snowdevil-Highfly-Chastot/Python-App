import math
import datetime

#Count is how many parts are left to be made
#Time is the amount of seconds it takes to machine a part

def runTimeLeft(count, time):
    
#Create blank dictionary
    totalTime = {}
    
#Function to cut down on repeat math
    def timeMath(seconds):

        if seconds == 0:
            return math.floor(count * time)
        else:
            return math.floor(count * time / seconds)
    
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
    
    print(totalTime)
        
    return totalTime

#Calculates date and time for the job to be done running
def completionTime(count, time):
    
#Setting date/time variables to calculate finish date/time
    now = datetime.datetime.now()
    jobFinished = now + datetime.timedelta(seconds = count * time)

    return jobFinished

#Calculates amount of parts possible to machine per bar	
def barfeedParts(partLength, cutoffWidth, barfeedParameter, barLength):
    
#Set variables and calculate parts needed to finish a bar
    actualPartLength = partLength + cutoffWidth
    actualBarLength = barLength - barfeedParameter
    totalParts = math.floor(actualBarLength / actualPartLength)

    return totalParts
    
import math
import datetime

#Count is how many parts are left to be made
#Time is the amount of seconds it takes to machine a part

def runTimeLeft(count, time):
	
	totalTime = []
	
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
		totalTime.append(["Days", dayTimeLeft])
	if hourTimeLeft > 0:
		totalTime.append(["Hours", hourTimeLeft])
	if minuteTimeLeft > 0:
		totalTime.append(["Minutes", minuteTimeLeft])
	if secondTimeLeft > 0:
		totalTime.append(["Seconds", secondTimeLeft])
        
	return totalTime

def completionTime(count, time):
	
#Setting date/time variables to calculate finish date/time
	now = datetime.datetime.now()
	jobFinished = now + datetime.timedelta(seconds = count * time)

	return jobFinished
	
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
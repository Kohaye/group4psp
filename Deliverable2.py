# CalcSpeedSound3pt0.py
# Created by: Korey Hayes
# 26 Nov 2020
# Calculates the speed of sound in salt water for a whale and the angle of that whale between 2 hydrophones
# Uses the temperature of the water (in degrees C), the depth of the whale (in meters)
# Uses the speed (in meters per second), distance (in meters) and time (in seconds) between the hydrophones
# to calculate the angle of the whale in radians
# Assumes salinity of the water is 35 PSA
# Inputs read from csv file
# Outputs written to new csv file

import math                                         # to calculate the angle of the whale
import csv                                          # to read from a csv file
# create a function to calculate the speed of sound in salt water
def SpeedSoundCalcFunction(input_depth, input_temperature):
    # speedsound list to hold calculated results
    calc_speedsound = []                            # create empty list

    # For each data set, calculate speed sound and add to speedsound list
    for index in range(len(input_depth)):   	    # index will be 0, 1, 2, ...
        # retrieve temperature in index position from input_temperature list
        functionTemperature = float(input_temperature[index])    
        functionDepth = float(input_depth[index])   # retrieve depth in index position from input_depth list
        
        # Calculate the speed of sound using the inputs
        SpeedSound = 1448.96 + (4.591 * (functionTemperature)) - ((5.304 * (10**-2)) * (functionTemperature**2)) \
        + ((2.374 * (10**-4)) * (functionTemperature**3)) + ((1.63 * (10**-2)) * functionDepth) \
        + ((1.675 * (10**-7)) * (functionDepth**2)) - ((7.139 * (10**-13)) * functionTemperature * (functionDepth**3))
        calc_speedsound.append(SpeedSound)          # add speedsound to calc_speedsound list
   
    return calc_speedsound                          #returns the populated list

# Create a function to calculate the angle of the whale
def whaleAngleCalcFunction(input_timediff, input_hydrophonedistance, speedSoundCalcList):

    calc_whaleAngle = []                            # create and empty list for the angle calculations

    for index in range(len(input_hydrophonedistance)):
        # assign each local variable to the indexed item in their corresponding list
        functionHydrophoneDistance = input_hydrophonedistance[index]
        functionTimeDiff = input_timediff[index]
        functionSpeedSound = speedSoundCalcList[index]
        # create an arbitrary variable for the calculation
        calc = (functionTimeDiff*functionSpeedSound)/functionHydrophoneDistance
        # calculate the angle of the whale using the local variables (inputs from main function)
        # angle = cos^-1((time*speed)/distance)
        # where time = functionTimeDiff, speed = functionSpeedSound, and distance = functionHydrophoneDistance
        # This can only work if time*speed < distance, so we create a selection statement
        if functionTimeDiff*functionSpeedSound < functionHydrophoneDistance:
            # run the math function with the calculated variable
            whaleAngle = math.acos(calc)
            # append the list with the rounded angle calculation
            calc_whaleAngle.append(format(whaleAngle, '.2f'))
        # show that the inputs caused an error, but allow the list to still populate
        else: calc_whaleAngle.append("err")
    return calc_whaleAngle                          # return the populated list


# Display program purpose
def main():
    print("This application calculates the speed of sound in salt water")
    print("Assumption:  salinity is 35 PSA")
    print()
    print('************************************************************') 
    print()
    tempList = []									# empty list to read the temperatures in from the csv
    depthList = []									# empty list to read the depth in from the csv
    timeList = []									# empty list to read the time in from the csv
    distList = []									# empty list to read the distance in from the csv

    whalefile = open(r"whaledata.csv")              # opens the file required to read the input
    freader = list(csv.reader(whalefile))			# sets the file that is read to a list of lists					
    whalefile.close()								# closes the file once the reader is done
    x = 1											# sets x to 1 because we don't want the first row of the csv
    while x<12:										# starts a loop to go through each row of the file
    	tempList.append(float(freader[x][0]))		# appends each list with the corresponding index of each row
    	depthList.append(float(freader[x][1]))
    	timeList.append(float(freader[x][2]))
    	distList.append(float(freader[x][3]))
    	x+=1										# iterates x
    ############### End of input, Start of calculations ################
    # Speed of Sound for each instance needs to be calculated first
    # Populate a new list of the returned results of the function
    speedSoundCalcList = SpeedSoundCalcFunction(depthList, tempList)
    # Whale Angle calculations are next
    # Populate a new list of the returned results of the function
    whaleAngleCalcList = whaleAngleCalcFunction(timeList, distList, speedSoundCalcList)

    print("---------------------------------------------------------------------------------")
    print()
    # Set column header line to it's own list
    headings = ["Temp(C)", "Depth(m)", "SoundSpeed(m/s)", "TimeDiff(s)", "HP Distance(m)", "Whale Angle(rad)"]
    newFile = []                                    # create empty list to write to csv
    newFile.append(headings)                        # append list to the list as first item
    writeFile = open(r"whaleWriteData.csv", "w")    # opens the csv file to write to it
    fwriter = csv.writer(writeFile)                 # set a variable to write to call the writing operation
    for index in range(len(speedSoundCalcList)):    # run a loop for the length of the inputs
        # set each row of variables to a new list of the items at the index
        writeList = [tempList[index], depthList[index], speedSoundCalcList[index], timeList[index], distList[index], whaleAngleCalcList[index]]
        newFile.append(writeList)                   # append the list of lists with the new row of items
    fwriter.writerows(newFile)                      # write the list of lists to the csv file
    print()
    print("Done")                                   # print statement for the end of the program
# check to see if the main function is being called within the program
if __name__ == '__main__':
    main()
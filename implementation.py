# Group 4 Problem Solving and Programming Python Script file
# Adding this comment in VS code at 2:10pm -> Korey Hayes
# Dan like Pandas
# Korey updated the CSV file to only contain relevant information
# to the program columns = year and month of that year
# Daily Discharge (m3/s) (PARAM = 1)
# St. Lawrence River At Cornwall
# This program is designed to read daily flow rates from a csv file and calculate the monthly and
# yearly totals at a specific monitoring station - St. Lawrence River at Cornwall
import csv                                  # csv used in week 12 for csv file reading/writing
import matplotlib                           # (available on college system as indicated on VDI)
flow = open(r"StLawrenceFlow.csv")          # opens the file required to read the input
freader = list(csv.reader(flow))			# sets the file that is read to a list of lists					
flow.close()								# closes the file once the reader is done
x = 1									    # sets x to 1 because we don't want the first row of the csv
y = 0                                       # sets y to 0 so we can compare yearChoice with index0 of freader
janflow =[]                                 # create an empty list for each month of the year
febflow =[]
marflow =[]
aprflow =[]
mayflow =[]
junflow =[]
julflow =[]
augflow =[]
sepflow =[]
octflow =[]
novflow =[]
decflow =[]
yearflow =[]                                # create an empty list for the flow of the whole year
# year number index = 0, jan = 1, feb = 2, ...... , dec = 12
yearChoice = int(input("Please enter the year you would like to calculate the flow rate for:  "))
for x, y in freader:
    if freader[x][y] == yearChoice:
        janflow.append(freader[x][y+1])
        febflow.append(freader[x][y+2]) 
        marflow.append(freader[x][y+3]) 
        aprflow.append(freader[x][y+4]) 
        mayflow.append(freader[x][y+5]) 
        junflow.append(freader[x][y+6]) 
        julflow.append(freader[x][y+7]) 
        augflow.append(freader[x][y+8]) 
        sepflow.append(freader[x][y+9]) 
        octflow.append(freader[x][y+10]) 
        novflow.append(freader[x][y+11]) 
        decflow.append(freader[x][y+12]) 
        # yearflow.append(freader[x][y+1]) 
print(janflow)

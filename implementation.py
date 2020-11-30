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
flow = open(r"C:\PSP\Group4\group4psp\StLawrenceFlow.csv")          # opens the file required to read the input
freader = list(csv.reader(flow))			# sets the file that is read to a list of lists					
flow.close()								# closes the file once the reader is done
x = 1									    # sets x to 1 because we don't want the first row of the csv
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
while x<1115:
    if freader[x][0] == yearChoice:
        print("maybe this is why")
        janflow.append(int(freader[x][1]))
        febflow.append(int(freader[x][2]))
        marflow.append(int(freader[x][3])) 
        aprflow.append(int(freader[x][4])) 
        mayflow.append(int(freader[x][5]))
        junflow.append(int(freader[x][6])) 
        julflow.append(int(freader[x][7])) 
        augflow.append(int(freader[x][8])) 
        sepflow.append(int(freader[x][9])) 
        octflow.append(int(freader[x][10])) 
        novflow.append(int(freader[x][11])) 
        decflow.append(int(freader[x][12])) 
        # yearflow.append(freader[x][y+1])
    x += 1
print(janflow)

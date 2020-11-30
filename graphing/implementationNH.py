#Graph to show the monthly discharge rate

import matplotlib
# import matplotlib.pyplot as plt

# Month= ["January","February","March","April","May","June","July","August","September","October","November","December"]
# Average = ['1','2','3','4','5','6','7','8','9','10','11','12']     #input list that includes all the mean averages

# input_year=1560
# r= ('The average monthly dischare shown per year', input_year)
# plt.scatter(Month,Average)
# plt.ylabel('Average Discharge')
# plt.xlabel('Month')
# plt.title(r)
# plt.show()



import csv                                  # csv used in week 12 for csv file reading/writing
import matplotlib                           # (available on college system as indicated on VDI)
flow = open(r"C:\PSPGroupAssignment\group4psp\StLawrenceFlow.csv")          # opens the file required to read the input
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
yearChoice = input("Please enter the year you would like to calculate the flow rate for:  ")
while x<1115:
    if freader[x][0] == yearChoice:
        if freader[x][1] != "":       # only append the list if there exists a value at this index
            janflow.append(int(freader[x][1]))
        if freader[x][2] !="":
            febflow.append(int(freader[x][2]))
        if freader[x][3] !="":
            marflow.append(int(freader[x][3]))
        if freader[x][4] !="":
            aprflow.append(int(freader[x][4]))
        if freader[x][5] !="":
            mayflow.append(int(freader[x][5]))
        if freader[x][6] !="":
            junflow.append(int(freader[x][6]))
        if freader[x][7] !="":
            julflow.append(int(freader[x][7]))
        if freader[x][8] !="":
            augflow.append(int(freader[x][8]))
        if freader[x][9] !="":
            sepflow.append(int(freader[x][9]))
        if freader[x][10] !="":
            octflow.append(int(freader[x][10]))
        if freader[x][11] !="":
            novflow.append(int(freader[x][11]))
        if freader[x][12] !="":
            decflow.append(int(freader[x][12]))
    x += 1
print(janflow, '\n', febflow, '\n',marflow, '\n',aprflow, '\n',mayflow, '\n',junflow, '\n',julflow, '\n',augflow, '\n',sepflow, '\n',octflow, '\n',novflow, '\n',decflow)

def Calcaverage(month):
    average=sum(month)/len(month)
    return average

print (Calcaverage(janflow))
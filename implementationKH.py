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
def plotGraph(input_year, average, yearlyav):
    import matplotlib.pyplot as plt
    yearlyav = str(round(yearlyav, 2))
    Month= ["January","February","March","April","May","June","July","August","September","October","November","December"]
    r= input_year
    plt.scatter(Month, average)
    plt.ylabel('Average Discharge (m³/s)')
    plt.xlabel('Month')
    plt.xticks(Month, rotation =45)
    plt.title('The Average Monthly Discharge of The St. Lawrence River \n At Cornwall Monitoring Station for the Year' + ' ' + r)
    plt.text(Month[8], 7200, 'Yearly Avg ='+ ' ' + yearlyav, fontsize = 9)
    # plt.text(Month[10], 7000, yearlyav)
    return plt.show()
    
def Calcaverage(month):
    average=round(sum(month)/len(month), 2)
    return average

def main():
    try:
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

        # yearflow =[]                                # create an empty list for the flow of the whole year
        # year number index = 0, jan = 1, feb = 2, ...... , dec = 12
        print("Hello! \n Seems like you want to calculate flow rates!")
        print("What year would you like to calculate the flow rates for?")
        yearChoice = int(input("Please enter a year between 1959 and 1993:  "))
        if yearChoice <1959 or yearChoice >1993:
            while yearChoice <1959 or yearChoice >1993:
                print ("Year choice must be between 1959 and 1993")
                print("Please re-enter values")
                yearChoice = int(input("Please enter a REALISTIC number between 1959 and 1993:  "))

        yearChoice = str(yearChoice)
        while x<1115:                               # cycle through all of the rows in the table
            if freader[x][0] == yearChoice:         # only append the lists if the item at this index = the inputted year
                if freader[x][1] != "":             # only append the list if there exists a value at this index
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

        # print(janflow, '\n', febflow, '\n',marflow, '\n',aprflow, '\n',mayflow, '\n',junflow, '\n',julflow, '\n',augflow, '\n',\
        #     sepflow, '\n',octflow, '\n',novflow, '\n',decflow)

        monthlyflow=[janflow,febflow,marflow,aprflow,mayflow,junflow,julflow,augflow,sepflow,octflow,novflow,decflow]
        averagemonthlyflow=[]
        for i in monthlyflow:
            average=Calcaverage(i)
            averagemonthlyflow.append(average)
        yearAvg = Calcaverage(averagemonthlyflow)
        print(averagemonthlyflow)
        print (yearAvg)
        # print(plotGraph(yearChoice, averagemonthlyflow, yearAvg))


        print("---------------------------------------------------------------------------------")
        print()
        print("The Average Monthly Discharge (m³/s) of the St. Lawrence River \n at Cornwall Monitoring Station for the Year" + " " + yearChoice)
        print()
        # Display the columns headers
        print("January\t\t February\t March\t\t April\t\t June\t\t July")
        print(averagemonthlyflow[0],"\t", averagemonthlyflow[1],"\t", averagemonthlyflow[2],"\t", averagemonthlyflow[3],"\t", \
            averagemonthlyflow[5], "\t", averagemonthlyflow[6],"\n")
        print("August\t\t September\t October\t November\t December\t Total Yearly Average")
        print(averagemonthlyflow[7],"\t", averagemonthlyflow[8],"\t", \
            averagemonthlyflow[9],"\t", averagemonthlyflow[10],"\t", averagemonthlyflow[11],"\t", yearAvg)
        print("---------------------------------------------------------------------------------")
    except TypeError:
        print("What are you trying to do here?")
    except ValueError: 
        print("You didn't enter a valid number, smart one")
    except RuntimeError: 
        print("You took too long, speedy one")
    except ZeroDivisionError:
        print("Stop trying to break the universe")
    except Exception as message:
        print(message)
if __name__ == '__main__':
    main()
# Group 4 Problem Solving and Programming Python Script file
# Adding this comment in VS code at 2:10pm -> Korey Hayes
<<<<<<< HEAD
# Dan like Pandas
# Korey updated the CSV file to only contain relevant information
# to the program columns = year and month of that year
import csv                                  # csv used in week 12 for csv file reading/writing
import matplotlib                           # (available on college system as indicated on VDI)
flow = open(r"StLawrenceFlow.csv")          # opens the file required to read the input
freader = list(csv.reader(flow))			# sets the file that is read to a list of lists					
flow.close()								# closes the file once the reader is done
x = 1									    # sets x to 1 because we don't want the first row of the csv
y = 1                                       # sets y to 1 because we don't want the first column of the csv
janflow = []                                # create an empty list for each month of the year
febflow = []
marflow = []
aprflow = []
mayflow = []
junflow = []
julflow = []
augflow = []
sepflow = []
octflow = []
novflow = []
decflow = []
yearflow = []                               # create an empty list for the flow of the whole year
=======
#import matplotlib availible on college system as accessed through vdi
# Dana like Pandas
>>>>>>> d860ddb3cc6d1929efe8324f01dd0a755072d254

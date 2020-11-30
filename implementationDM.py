# Group 4 Problem Solving and Programming Python Script file
# Adding this comment in VS code at 2:10pm -> Korey Hayes
# Dan like Pandas
# Korey updated the CSV file to only contain relevant information
# to the program columns = year and month of that year
# Daily Discharge (m3/s) (PARAM = 1)
# St. Lawrence River At Cornwall
# This program is designed to read daily flow rates from a csv file and calculate the monthly and
# yearly totals at a specific monitoring station - St. Lawrence River at Cornwall

# Program File Name: implementation.py
# Authors: Group 4 - Dana McKee, Korey Hayes, Riley Sweeney, Natalia Hrynko
# Date: November 30, 2020

# 

# Program Purpose: "why/purpose of the code" The program is designed to read daily flow rates from a CSV file and calculate the monthly and
# yearly totals at a specific monitoring station, St. Lawrence River at Cornwall
# Assumptions: User wants daily flow rates from the St. Lawrence River at Cornwall


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


# User Inputs: 
# File Inputs: Daily Discharge (m3/s), Monthly Discharge, and Yearly Discharge (m3/s) from CSV file
# Outputs: Monthly Discharge, and Yearly Discharge (m3/s) from CSV file

# References: 
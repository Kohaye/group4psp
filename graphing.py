#Graph to show the monthly discharge rate

import matplotlib
import matplotlib.pyplot as plt

Month= ["January","February","March","April","May","June","July","August","September","October","November","December"]
Average = ['1','2','3','4','5','6','7','8','9','10','11','12']     #input list that includes all the mean averages

input_year=1560
r= ('The average monthly dischare shown per year', input_year)
plt.scatter(Month,Average)
plt.ylabel('Average Discharge')
plt.xlabel('Month')
plt.title(r)
plt.show()
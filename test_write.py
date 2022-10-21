
# Python program to demonstrate 
# writing to CSV 
    
# import numpy as np    
import csv
from re import I  

# name of csv file  
filename = "averg_file.csv"

# field names  
fields = ['Number_1',"Number_2"]  

with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  


for i in range(100):
    number = i
    number2 = i +1
        
    # writing to csv file  
    with open(filename, 'a') as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
            
        # writing the data rows  
        csvwriter.writerow([str(number), str(number2)])
      
# data rows of csv file  
rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']]  
      


# Python program to demonstrate 
# writing to CSV 
    
# import numpy as np    
import csv
from re import I  

# name of csv file  
filename = "averg_file.csv"

f = open(filename,'w')

for i in range(100):
    number = i
    number2 = i +1
        
    f = open(filename,'a')
    f.write(str(number),str(number2))
    # f.write(str(number2)) 
    f.write('\n')
    ## Python will convert \n to os.linesep
    f.close()
      

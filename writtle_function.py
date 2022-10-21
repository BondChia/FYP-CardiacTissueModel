def writile(timenotation,aaa) :




    open(14,file=filename,status="unknown")
        do i=1,m
            do j=1,m
                write(14,*) i,j,aaa(i,j)
	        enddo
        enddo
        #write(14,'(1x,256f8.4)') ((aaa(i,j),i=1,m),j=1,m)
    close(14)  
return


# call writile(timepameter(i),u(1:m,1:m))

filename = f"{timenotation}.csv"

# field names  
fields = ['i','j','u[]']  

with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  


for i in range(m)
    for j in range(m)
        with open(filename, 'a') as csvfile:  
                # creating a csv writer object  
                csvwriter = csv.writer(csvfile)  
                    
                # writing the data rows  
                csvwriter.writerow([str(i),str(j),str(u[i,j])])
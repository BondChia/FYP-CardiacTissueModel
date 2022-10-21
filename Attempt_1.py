import numpy as np
import math
import csv

a = 0.15
mu1 = 0.2
mu2 = 0.3
kk = 8.0
eps = 0.002

ka = 0.1
kb =0.5
kc = 1
afa = 1
bate = 2

m = 200
n = 4 # !400
omg0 = 2*math.pi/33.74

#Panfilov_equation
#Euler forward for Panfilov equation:
#du/dt=f(u,v)+Dfu*(dd(u)/dxx+dd(u)/dyy)
#dv/dt=g(u,v)+Dfv*(dd(v)/dxx+dd(v)/dyy)

u = u_new = np.zeros((m+1,m+1))
v = v_new = np.zeros((m,m))
q = q_new = np.zeros((m,m))

tt = [10, 60, 100, 200]
timepameter = ['1','2','3','4']
h=0.03
xL=350.0 
yL=350.0
dx=xL/m
dy=yL/m
dx2=dx*dx
dy2=dy*dy
Dfu=1.0

nstep = 201/h #####      nstep=int(201/h,4) 

#initial conditions

u[92:97,1:int((m+30)/2)] = 1.0
v[92:97,1:int((m+30)/2)] = 0.0
q[92:97,1:int((m+30)/2)] = 0.0

u[98:103,1:int((m+30)/2)] = 0.7
v[98:103,1:int((m+30)/2)] = 0.6
q[98:103,1:int((m+30)/2)] = 0.1

u[104:109,1:int((m+30)/2)] = 0.0
v[104:109,1:int((m+30)/2)] = 0.8
q[104:109,1:int((m+30)/2)] = 0.2

temp = 0

averg_file = "averg_file.xlsx"
data_file = "data_file.xlsx"

# field names  
fields = ['Iteration','q','u']  

with open(averg_file, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  

# field names  
fields = ['Data']  

with open(data_file, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  

def funcf(uu,vv,qq) :
    funcf_result = -kk*uu*(uu-a)*(uu-1)-uu*vv+ka*(afa+3*bate*qq**2)*uu
    return funcf_result

def funcg(uu,vv) :
    funcg_result = (eps+(mu1*vv)/(mu2+uu))*(-vv-kk*uu*(uu-a-1))
    return funcg_result

def funcq(uu,qq) :
    funcq_result = kb*uu-kc*qq
    return funcq_result


for ncount in range(int(nstep)) :
    #no-flux boundary condition
    u[0,1:m] = u[1,1:m]
    u[m,1:m] = u[m,1:m]
    u[1:m,0] = u[1:m,1]
    u[1:m,m] = u[1:m,m]     

    averg = 0
    number = 0

    for i in range(m):
        for j in range(m):
            u_new[i,j] = u[i,j] + h*funcf(u[i,j],v[i,j],q[i,j]) + h*Dfu*(u[i+1,j]+u[i-1,j]-2*u[i,j])/dx2 + h*Dfu*(u[i,j+1]+u[i,j-1]-2*u[i,j])/dy2
            v_new[i,j]=v[i,j]+h*funcg(u[i,j],v[i,j])
            q_new[i,j]=q[i,j]+h*funcq(u[i,j],q[i,j])

            averg = averg + u_new[i,j]

            if (u[100,100] >= 0.04) :
                number += 1
            # writing to csv file  
            with open(averg_file, 'a') as csvfile:  
                # creating a csv writer object  
                csvwriter = csv.writer(csvfile)  
                    
                # writing the data rows  
                csvwriter.writerow([str(ncount*h),str(q[100,100]),str(u[100,100])])
            
            with open(data_file, 'a') as csvfile:  
                # creating a csv writer object  
                csvwriter = csv.writer(csvfile)  
                    
                # writing the data rows  
                csvwriter.writerow([str(number)])
      
            print(f"Iteration :{ncount*h} , Value:{averg/(256*256)}")
      
            for i in range(n) :
                if (ncount == tt[i]/h) :
                    temp += 0
                    filename = f"{timepameter(i)}.csv"

                    # field names  
                    fields = ['i','j','u[]']  

                    with open(filename, 'w') as csvfile:  
                        # creating a csv writer object  
                        csvwriter = csv.writer(csvfile)  
                            
                        # writing the fields  
                        csvwriter.writerow(fields)  

                    for i in range(m):
                        for j in range(m):
                            with open(filename, 'a') as csvfile:  
                                    # creating a csv writer object  
                                    csvwriter = csv.writer(csvfile)  
                                        
                                    # writing the data rows  
                                    csvwriter.writerow([str(i),str(j),str(u[i,j])])
    u = u_new
    v = v_new
    q = q_new


# def writile(timenotation,aaa) :
#     # open(14,file=filename,status="unknown")
#     #     do i=1,m
#     #         do j=1,m
#     #             write(14,*) i,j,aaa(i,j)
# 	#         enddo
#     #     enddo
#     #     #write(14,'(1x,256f8.4)') ((aaa(i,j),i=1,m),j=1,m)
#     # close(14)  
#     print("hello")
#     return

# Noise Making 
# def gasdev(idum) :
#     if (iset == 0) :
#         v1 = 2*ran1(idum)-1
#         v2 = 2*ran1(idum)-1
#         rsq = v1**2+v2**2
#         if(rsq >= 1 or rsq == 0) :
#             v1 = 2*ran1(idum)-1
#             v2 = 2*ran1(idum)-1
#             rsq = v1**2+v2**2    
#         fac=math.sqrt(-2.*math.log(rsq)/rsq)
#         gset=v1*fac
#         gasdev=v2*fac
#         iset=1
#     else :
#         gasdev=gset
#         iset = 0
#     return



# def ran1(idum) :
#     IA=16807
#     IM=2147483647
#     AM=1/IM
#     IQ=127773
#     IR=2836
#     NTAB=32
#     NDIV=1+(IM-1)/NTAB
#     EPS=1.2e-7
#     RNMX=1.-EPS

#     iv = np.zeros(NTAB)
#     iy = 0

#     if (idum <= 0 or iy == 0) :
#         idum = max(-idum,1)
#         for j in range(NTAB+8) : #do 11 j=NTAB+8,1,-1
#             k=idum/IQ
#             idum=IA*(idum-k*IQ)-IR*k
#             if (idum < 0) :
#                 idum += IM
#             if (j <= NTAB) :
#                 iv[j]=idum
#             continue
#         iy = iv[1]

#     k=idum/IQ
#     idum=IA*(idum-k*IQ)-IR*k        
    
#     if(idum < 0) :
#         idum += IM
#     j = 1+iy/NDIV
#     iy = iv[j]
#     iv[j]=idum
#     ran1=min(AM*iy,RNMX)
#     return

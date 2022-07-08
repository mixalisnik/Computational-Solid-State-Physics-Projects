import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import time as time
np.random.seed(4404)
t1=time.time()
N=100
#p=0.56
pmax=0.8
dp=0.1
pc=0.59
p_mat=np.linspace(0.1,0.8,8)
np.random.seed(4408)
p_mat1=np.linspace(0.5,0.69,20)
p1=np.append(p_mat,[p_mat1])
p1=np.sort(p1)
p1=np.unique(p1)

pm1=[]
pm2=[]
pm3=[]
for p in p1:
    
    grid=np.zeros([N+1,N+1])
    # grid=np.array([[0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0,1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    # [0,1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    # [0,1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    # [0,0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    # [0,0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    # [0,0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    # [0,1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    # [0,1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    # [0,1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    # [0,1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    # [0,1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    # [0,0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    # [0,1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    # [0,1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    # [0,0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
    # [0,0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    # [0,1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    # [0,1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    # [0,0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    # [0,0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1]])
    for j in range(1,N+1):
        for i in range(1,N+1):
            r=np.random.rand()
            if r<p:
                grid[i,j]=1
    
    #CMLT
    k=1
    L=np.zeros([(N+1)**2])
    
    S=np.zeros([(N+1)**2])
    for j in range(1,N+1):
        for i in range(1,N+1):
            if grid[i,j]==0:
                continue;
            else:
                if grid[i,j-1]==0:
                    if grid[i-1,j]==0:
                        L[k]=k
                        grid[i,j]=L[k]
                        S[int(L[int(grid[i,j])])]=S[int(L[int(grid[i,j])])]+1
                        k=k+1
                    else:
                        grid[i,j]=L[int(grid[i-1,j])]
                        S[int(L[int(grid[i,j])])]=S[int(L[int(grid[i,j])])]+1
                else:
                    grid[i,j]=L[int(grid[i,j-1])]
                    S[int(L[int(grid[i,j])])]=S[int(L[int(grid[i,j])])]+1
                    if grid[i-1,j]==0 or grid[i-1,j]==L[int(grid[i,j-1])]:
                        continue;
                    else:
                        
                        for ks in range(1,np.size(L)):
                            if L[ks]==grid[i-1,j]:
                                L[ks]=L[int(grid[i,j-1])]
                        S[int(L[int(grid[i,j-1])])]=S[int(L[int(grid[i,j-1])])]+S[int(int(grid[i-1,j]))]
                        S[int(int(grid[i-1,j]))]=0
                    
    
        
    # temphelp=np.array([[0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0,1, 0, 6, 5, 0, 0, 0, 18 ,18, 0 ,26, 0, 33, 0, 0, 0 ,43, 31, 0, 52],
    # [0,1, 1, 1, 5, 0, 13, 0, 0, 0, 24, 0, 30, 11, 31, 31, 31, 31, 0, 49, 31],
    # [0,1, 0, 1, 0, 10, 5, 0 ,0 ,0 ,24 ,11 ,11 ,11 ,31 ,31 ,31 ,31 ,0 ,49 ,0],
    # [0,0, 5, 5, 5, 5, 0, 0, 19, 11, 11 ,11, 0, 11 ,31, 31, 31 ,31, 0, 49, 31],
    # [0,0, 0, 0, 0, 5, 5, 11 ,11 ,0 ,11 ,0 ,31 ,31 ,0 ,0, 0 ,31 ,0 ,49 ,31],
    # [0,0, 0, 0, 0, 0, 5, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 31, 31, 31, 0],
    # [0,2, 2, 3, 0, 0, 5, 11, 11, 11, 0 ,27 ,27, 0, 37 ,37, 37, 0, 0, 31, 0],
    # [0,2, 2, 3, 0, 11, 11, 11, 11, 11, 0, 27, 0, 34, 0, 0, 0, 0, 0, 31, 31],
    # [0,2, 2, 0, 0, 11, 11, 0, 0, 0, 0, 27, 27, 0, 38, 0, 0, 0, 0, 0, 31],
    # [0,2, 0, 7, 0, 0, 11, 0, 20, 14, 14, 0, 0, 0, 38, 38, 0, 0, 0, 50, 50],
    # [0,2, 2, 0, 9, 4, 0, 15, 14, 14, 14, 0, 32, 0, 0, 38, 38, 38, 0, 0, 0],
    # [0,0, 2, 3, 3, 4, 0, 15, 0, 14, 0, 28, 0, 35, 0, 38, 38, 0, 0, 0, 53],
    # [0,3, 3, 3, 0, 0, 14, 14, 0, 0, 0, 0, 0, 35, 0, 0, 38, 0, 46, 0, 53],
    # [0,3, 3, 3, 3, 4, 0, 0, 21, 4, 0, 29, 22, 22, 22, 22, 0, 44, 0 ,0 ,53,],
    # [0,0, 3, 0, 3, 4, 0, 16, 4, 4, 22, 22, 22, 22, 22, 22, 0, 0, 47, 0, 53],
    # [0,0, 3, 0, 3, 4, 4, 4, 0, 4, 22, 0, 22, 0, 22, 0, 41, 0, 47, 42, 42],
    # [0,4, 0, 8, 4, 0, 0, 0, 22, 22, 22, 22, 0, 0, 0, 40, 40, 0, 47, 42, 42],
    # [0,4, 4, 4, 0, 0, 0, 17, 0, 22, 0 ,22, 0, 0, 39, 0, 0, 45, 42, 0, 42],
    # [0,0, 4, 4, 4, 0, 0, 17, 0, 0, 25, 0, 0, 0, 39, 0, 42, 42, 0, 51, 0],
    # [0,0, 0, 4, 0, 12, 0, 0, 23, 23, 0, 0, 0, 36, 36, 36, 0, 0, 48, 48, 48]])
    # for i in range(N+1):
    #     for j in range(N+1):
    #         if grid[i,j]==temphelp[i,j]:
    #             print("TRUE")
    for j in range(1,N+1):
        for i in range(1,N+1):
            if grid[i,j]==0:
                continue;
            else:
                grid[i,j]=L[int(grid[i,j])]   
                
    mmax=np.max(S)
    I=np.sum(np.multiply(S,S)/(p*N**2))
    pm2.append(I) #I 
    
    pmax=mmax/(p*N*N)
    pm3.append(I-pmax*mmax) #Ι without biggest cluster
    pm1.append(pmax) #Pmax
plt.figure()
plt.plot(p1,pm1) #pmax
plt.figure() 
plt.plot(p1,pm2) #I
plt.figure()
plt.plot(p1,pm3) #I-largest cluster
plt.show()
time_elapsed=time.time()-t1
print(time_elapsed)

plt.figure()
p_lcr=abs(p1[8:12]-pc)
plt.plot(np.log(p_lcr),np.log(pm2[8:12]),'.')
res1 = stats.linregress(np.log(p_lcr),np.log(pm2[8:12]))
plt.plot(np.log(p_lcr), res1.intercept + res1.slope*np.log(p_lcr), 'r', label='Least-squares line')
plt.xlabel('log(p)')
plt.ylabel('log(I)')



plt.figure()
p_lcr=abs(p1[14:17]-pc)
plt.plot(np.log(p_lcr),np.log(pm3[14:17]),'.')
res2 = stats.linregress(np.log(p_lcr),np.log(pm3[14:17]))
plt.plot(np.log(p_lcr), res2.intercept + res2.slope*np.log(p_lcr), 'r', label='Least-squares line')
plt.xlabel('log(p)')
plt.ylabel('log(Ipr)')

plt.figure()
p_lcr=abs(p1[8:12]-pc)
plt.plot(np.log(p_lcr),np.log(pm1[8:12]),'.')
res3 = stats.linregress(np.log(p_lcr),np.log(pm1[8:12]))
plt.plot(np.log(p_lcr), res3.intercept + res3.slope*np.log(p_lcr), 'r', label='Least-squares line')
plt.xlabel('log(p)')
plt.ylabel('log(P)')
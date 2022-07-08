import matplotlib.pyplot as plt
import numpy as np

#Erdos Renyi
N=1000
n=100
p=1/6
S=0
S1=np.zeros(N-1)
np.random.seed(4408)
maxk=0
histdat=np.zeros(N-1)
smin=1
for k in range(n):
    grid=np.zeros([N,N])
    S1=np.zeros(N)
    for i in range(1,N):
        for j in range(i+1,N):
            r=np.random.rand()
            if r<p:
                grid[i,j]=1
                grid[j,i]=1
    S1=S1+np.sum(grid,1)
    smax=int(S1.max())
    if smax>maxk:
        maxk=smax
    
    for i in range(smin,smax+1):
        histdat[i]=histdat[i]+np.count_nonzero(S1==i)
        
        

kappa=np.arange(smin,maxk+1)
plt.figure(2)    
plt.scatter(kappa,histdat[:maxk]/(n**2))
plt.xlabel("k")
plt.ylabel("P(k)")
plt.title("Erdos Renyi Network P(k)-k")
plt.axvline(166.67,color='coral')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

N=1000
grid=np.zeros([N,N])
k=14
n1=90
#Matrix Initialization
for i in range(N):
    if i+int(k/2)<N:
        grid[i,i+1:i+int(k/2)+1]=1
    else:
        grid[i,:(i+int(k/2))%N+1]=1
        grid[i,i+1:N]=1
for i in range(N):
    if i-int(k/2)>0:
        grid[i,i-1:i-int(k/2)-1:-1]=1
    elif i-int(k/2)==0:
        grid[i,:int(k/2)]=1
    else:
        grid[i,:i]=1
        grid[i,i-int(k/2):N]=1
# for p probability, redistribute connections

p=0.2
S=np.sum(grid,axis=1)
smin=1
histdat=np.zeros(N-1)
maxk=0
for n in range(n1):
    grid1=grid.copy()
    #S1=S.copy()
    S1=np.zeros(N)
    for i in range(N):
        for j in range(N):
            if grid1[i][j]!=0:
                r=np.random.rand()
                if r<p:
                    grid1[i][j]=0#break the connection
                    grid1[j][i]=0
                    connect=0
                    while connect==0:
                        r1=np.random.randint(0,N-1)#connect new
                        if grid1[i][r1]==0 and i!=r1: #If no connection: Connect nodes
                            grid1[i][r1]=1
                            grid1[r1][i]=1
                            connect=1
    S1=S1+np.sum(grid1,axis=1)
    smax=int(S1.max())
    if smax>maxk:
        maxk=smax
    
    for i in range(smin,smax+1):
        histdat[i]=histdat[i]+np.count_nonzero(S1==i+1)


kappa=np.arange(smin,maxk)
plt.figure(2)    
plt.scatter(kappa,histdat[:maxk-1])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.title("Small World Network P(k)-k")
plt.axvline(14,color='coral')
plt.show()
                
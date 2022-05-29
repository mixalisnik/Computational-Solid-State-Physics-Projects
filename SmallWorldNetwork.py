import numpy as np
import matplotlib.pyplot as plt

N=1000
grid=np.zeros([N,N])
k=14
n1=50
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
S=0

for n in range(n1):
    grid1=grid.copy()
    for i in range(N):
        for j in range(N):
            if grid1[i][j]==0:
                continue
            else:
                r=np.random.rand()
                if r<p:
                    grid1[i][j]=0#break the connection
                    grid1[j][i]=0
                    connect=0
                    while connect==0:
                        r1=np.random.randint(0,N)#connect new
                    
                        if grid1[i][r1]==0 and i!=r1: #If no connection: Connect nodes
                            grid1[i][r1]==1
                            grid1[r1][i]==1
                            connect=1
    S=S+np.sum(grid1,axis=1)
    
#     #S1=S1+S
S=S/n1
plt.hist(S, density = True)

# plt.show()
                
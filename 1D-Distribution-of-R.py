import numpy as np
from matplotlib import pyplot as plt 


#1 dimension Random Walk
n=10000
steps=1000
grid_num=1000000
pos_x=np.random.randint(0,grid_num)

mean_mat1=np.zeros([n,1])


for j in range(n):
    pos_xo=pos_x
    for i in range(steps):
        if pos_x!=0 and pos_x!=grid_num:
            pos_x=pos_x+np.random.choice([-1,1])
        elif pos_x==0:
            pos_x=pos_x+1
        elif pos_x==grid_num:
            pos_x=pos_x-1
        
    delta_x=pos_x-pos_xo
    r1=delta_x
    mean_mat1[j]=r1
plt.figure(0)
plt.title('Distribution of R')
plt.hist(mean_mat1,bins=20,alpha=0.4,label='N=1000')
#plt.hist(mean_mat1[0:int(n/2)],bins='auto')
plt.grid()
#plt.show()

n=10000
steps=2000
grid_num=1000000
pos_x=np.random.randint(0,grid_num)

mean_mat1=np.zeros([n,1])


for j in range(n):
    pos_xo=pos_x
    for i in range(steps):
        if pos_x!=0 and pos_x!=grid_num:
            pos_x=pos_x+np.random.choice([-1,1])
        elif pos_x==0:
            pos_x=pos_x+1
        elif pos_x==grid_num:
            pos_x=pos_x-1
        
    delta_x=pos_x-pos_xo
    r1=delta_x
    mean_mat1[j]=r1
plt.figure(0)
plt.title('Distribution of R')
plt.hist(mean_mat1,bins=20,alpha=0.4,color='c',label='N=2000')
#plt.hist(mean_mat1[0:int(n/2)],bins='auto')
plt.grid()
plt.show()


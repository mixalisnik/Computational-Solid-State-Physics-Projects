import numpy as np
from matplotlib import pyplot as plt 
np.random.seed(4408)
#2 dimension Random Walk
n=10000
steps=1000
grid_num=1000
pos_x=np.random.randint(0,grid_num+1)
pos_y=np.random.randint(0,grid_num+1)
s_mat=np.zeros([int(steps/100)+1,1])
t=np.linspace(0,1000,int(steps/100)+1)

for j in range(n):

    occ=np.zeros([grid_num+1,grid_num+1])
    pos_xo=pos_x
    pos_yo=pos_y
    occ[pos_xo,pos_yo]=1
    
    for i in range(steps+1):
        r=np.random.rand()
        
        if r<=0.5:
            if pos_x!=0 and pos_x!=grid_num:
                pos_x=pos_x+np.random.choice([-1,1])
            elif pos_x==0:
                pos_x=pos_x+1
            elif pos_x==grid_num:
                pos_x=pos_x-1
        else:
            if pos_y!=0 and pos_y!=grid_num:
                pos_y=pos_y+np.random.choice([-1,1])
            elif pos_y==0:
                pos_y=pos_y+1
            elif pos_y==grid_num:
                pos_y=pos_y-1
        
        occ[pos_x,pos_y]=1
        if i%100==0:
            s_mat[int(i/100)]=s_mat[int(i/100)]+np.sum(occ)

s_mat=s_mat/n
plt.title('Unique Sites Visited S - Steps')
x=np.linspace(5,1000,1000)
y1=np.pi*x/np.log(x)
plt.ylabel('Sites (S(N))')
plt.xlabel('steps (N)')
plt.plot(x,y1,label='Theoretical S curve')
plt.scatter(t,s_mat,label='Simulated S Points')
plt.grid()
plt.show()

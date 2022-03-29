import numpy as np
from matplotlib import pyplot as plt 

#2 dimension Random Walk
n=2
steps=1000
grid_num=500

pos_x=np.random.randint(0,grid_num+1)
pos_y=np.random.randint(0,grid_num+1)
pos_z=np.random.randint(0,grid_num+1)
s_mat=np.zeros([int(steps/100)+1,1])
t=np.linspace(0,1000,int(steps/100)+1)

for j in range(n):

    occ=np.zeros([grid_num+1,grid_num+1,grid_num+1])
    pos_xo=pos_x
    pos_yo=pos_y
    pos_zo=pos_z
    occ[pos_xo,pos_yo,pos_zo]=1
    
    for i in range(steps+1):
        r=np.random.rand()        
        if r<=0.33:
            if pos_x!=0 and pos_x!=grid_num:
                pos_x=pos_x+np.random.choice([-1,1])
            elif pos_x==0:
                pos_x=pos_x+1
            elif pos_x==grid_num:
                pos_x=pos_x-1
                
        elif r<=0.66:
            if pos_y!=0 and pos_y!=grid_num:
                pos_y=pos_y+np.random.choice([-1,1])
            elif pos_y==0:
                pos_y=pos_y+1
            elif pos_y==grid_num:
                pos_y=pos_y-1
        
        else:
            if pos_z!=0 and pos_z!=grid_num:
                pos_z=pos_z+np.random.choice([-1,1])
            elif pos_z==0:
                pos_z=pos_z+1
            elif pos_z==grid_num:
                pos_z=pos_z-1
        
        occ[pos_x,pos_y,pos_z]=1
        if i%100==0:
            s_mat[int(i/100)]=s_mat[int(i/100)]+np.sum(occ)

s_mat=s_mat/n
plt.title('Unique Sites Visited S - Steps')
plt.scatter(t,s_mat,label='Simulated S Points')
x=np.linspace(0,1000,1000)
y2=0.66*x
plt.plot(x,y2,label='Theoretical S curve')
plt.legend()
plt.grid()
plt.show()
import numpy as np
from matplotlib import pyplot as plt 


#1 dimension Random Walk
n=10000
steps=1000
grid_num=1000
pos_x=np.random.randint(0,grid_num+1)
s_mat=np.zeros([int(steps/100)+1,1])
t=np.linspace(0,1000,int(steps/100)+1)


for j in range(n):
    occ=np.zeros([grid_num+1,1])
    pos_xo=pos_x
    occ[pos_xo]=1
    
    for i in range(steps+1):
        
        if pos_x!=0 and pos_x!=grid_num:
            pos_x=pos_x+np.random.choice([-1,1])
            
        elif pos_x==0:
            pos_x=pos_x+1
            
        elif pos_x==grid_num:
            pos_x=pos_x-1
            
        occ[pos_x]=1
        if i%100==0:
            s_mat[int(i/100)]=s_mat[int(i/100)]+np.sum(occ)
            
            
        
s_mat=s_mat/n
plt.title('Unique Sites Visited S - Steps')
plt.scatter(t,s_mat,label='Simulated S Points')
x=np.linspace(0,1000,1000)
y=np.sqrt(8*x/np.pi)
plt.ylabel('Sites (S(N))')
plt.xlabel('steps (N)')
plt.plot(x,y,label='Theoretical S curve')
plt.legend()
plt.grid()
plt.show()


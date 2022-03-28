import numpy as np

#1 dimension Random Walk
steps=1000
grid_num=1000
pos_x=np.random.randint(0,grid_num)
n=10000
mean_mat1=np.zeros([steps,1])
r_squared=0
nt=0
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
    r_squared=r_squared+delta_x**2
    nt=nt+1
res=r_squared/nt


import numpy as np

np.random.seed(4408)
#2 dimension Random Walk
n=1000
steps=1000
grid_num=1000
pos_x=np.random.randint(0,grid_num)
pos_y=np.random.randint(0,grid_num)


r_squared=0
nt=0
for j in range(n):
    pos_xo=pos_x
    pos_yo=pos_y
    
    for i in range(steps):
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
      
        
            
    delta_x=pos_x-pos_xo
    delta_y=pos_y-pos_yo
    r_squared=r_squared+delta_x**2 +delta_y**2
    nt=nt+1
res=r_squared/nt

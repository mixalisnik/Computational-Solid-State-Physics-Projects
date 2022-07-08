import numpy as np
from matplotlib import pyplot as plt 
np.random.seed(4408)
#2 dimension Random Walk
n=1000
steps=1000
grid_num=1000
pos_x=np.random.randint(0,grid_num)
pos_y=np.random.randint(0,grid_num)
x_points=np.linspace(0,steps,int(steps/100)+1)
delta_x=np.zeros([int(steps/100)+1,1])
delta_y=np.zeros([int(steps/100)+1,1])
r_squared=np.zeros([int(steps/100)+1,1])


for j in range(n):
    pos_xo=pos_x
    pos_yo=pos_y
    
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
        
        if i%100==0:
            delta_x[int(i/100)]=pos_x-pos_xo
            delta_y[int(i/100)]=pos_y-pos_yo
            r_squared[int(i/100)]=r_squared[int(i/100)]+delta_x[int(i/100)]**2+delta_y[int(i/100)]**2
            
plt.figure()
plt.title('R squared average - steps 2D')
plt.xlabel('steps')
plt.ylabel('R squared average')
plt.scatter(x_points,r_squared/n)
a,b=np.polyfit(x_points,r_squared/n,1)
x_row=np.linspace(0,1000,1000)
y=a*x_row+b
plt.plot(x_row,y,c='red')
plt.grid()
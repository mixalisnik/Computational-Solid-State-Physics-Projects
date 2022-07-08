import numpy as np
from matplotlib import pyplot as plt 
np.random.seed(4408)

#1 dimension Random Walk
n=1000
steps=1000
grid_num=1000
pos_x=np.random.randint(0,grid_num)
x_points=np.linspace(0,steps,int(steps/100)+1)
delta_x=np.zeros([int(steps/100)+1,1])
r_squared=np.zeros([int(steps/100)+1,1])

for j in range(n):
    pos_xo=pos_x
    for i in range(steps+1):
        if pos_x!=0 and pos_x!=grid_num:
            pos_x=pos_x+np.random.choice([-1,1])
        elif pos_x==0:
            pos_x=pos_x+1
        elif pos_x==grid_num:
            pos_x=pos_x-1
        if i%100==0:
            delta_x[int(i/100)]=pos_x-pos_xo
            r_squared[int(i/100)]=r_squared[int(i/100)]+delta_x[int(i/100)]**2
            
plt.figure()
plt.title('R squared average - steps 1D')
plt.xlabel('steps')
plt.ylabel('R squared average')
plt.scatter(x_points,r_squared/n)     
a,b=np.polyfit(x_points,r_squared/n,1)
x_row=np.linspace(0,steps,1000)
y=a*x_row+b
plt.plot(x_row,y,c='red')
plt.grid()


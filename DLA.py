import numpy as np
import matplotlib.pyplot as plt
np.random.seed(4408)
import time as time
t1=time.time()
def delta_x(x,xo):
    return x-xo
def delta_y(y,yo):
    return y-yo

def randomwalk2d(grid_num,pos_x,pos_y):
    #2 dimension Random Walk   
        
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
    return pos_x,pos_y
grid_size=50
xo=int(grid_size/2)
yo=xo
grid1=np.zeros([grid_size,grid_size])
grid1[xo,yo]=1
radius=200
tolerance=0.01


row=[]
col=[]
plt.figure()
plt.grid()
plt.title("DLA Structure Simulation")
plt.xlabel("x Position")
plt.ylabel("y Position")
#Find Initial Possible Positions
for i in range(grid_size):
    for j in range(grid_size):
        if abs(delta_x(i,xo)) + abs(delta_y(j,yo))==radius:
            row.append(i)
            #row.append(j)
            col.append(j)
            #col.append(i)
            #grid1[i,j]=1

          

finished=0
plt.xlim(xo-1*radius,xo+1*radius)
plt.ylim(xo-1*radius,xo+1*radius)
nplaced=0
while finished==0:
    r1=np.random.randint(0,np.size(row)) #Choose starting point
    pos_x=row[r1]
    pos_y=col[r1]            

    stuck=0 #Flag particle as not stuck
    while stuck==0:
        pos_x_new,pos_y_new=randomwalk2d(grid_size, pos_x, pos_y)
        if grid1[pos_x_new-1,pos_y_new]==1 or grid1[pos_x_new+1,pos_y_new]==1 or grid1[pos_x_new,pos_y_new-1]==1 or grid1[pos_x_new,pos_y_new+1]==1:
            stuck=1
            grid1[pos_x_new,pos_y_new]=1
            nplaced=nplaced+1
            if abs(delta_x(pos_x_new,xo)) + abs(delta_y(pos_y_new,yo))>=radius:
                finished=1
            break;
        if abs(delta_x(pos_x_new,xo)) + abs(delta_y(pos_y_new,yo))>=(1+tolerance)*radius: #if out of bounds, rechoose starting position
            r1=np.random.randint(0,np.size(row)) #Choose starting point
            pos_x=row[r1]
            pos_y=col[r1]
        else:
            pos_x=pos_x_new
            pos_y=pos_y_new
    plt.scatter(pos_x_new,pos_y_new,c='coral',marker=".",s=3)
time_elapsed=time.time()-t1
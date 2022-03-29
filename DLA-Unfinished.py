import numpy as np
import matplotlib.pyplot as plt
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


grid_size=450
xo=int(grid_size/2)
yo=xo
grid1=np.zeros([grid_size,grid_size])
grid1[xo,yo]=1
radius1=25
tolerance=0.01
row=[]
col=[]
posmat=[]
#Plot Circle
for i in range(grid_size):
    for j in range(grid_size):
        if delta_x(i,xo)**2 + delta_y(j,yo)**2==radius1**2:
            row.append(i)
            row.append(j)
            col.append(j)
            col.append(i)
            
plt.figure()
plt.axhline(y=0,xmin=0,xmax=450)
plt.axhline(y=450,xmin=0,xmax=450)
plt.axvline(x=0,ymin=0,ymax=450)
plt.axvline(x=450,ymin=0,ymax=450)
circle1=plt.Circle((xo,yo),radius1,fill=False)
ax=plt.gca()
ax.set_xlim((200,250))
ax.set_ylim((200,250))
ax.add_patch(circle1)

plt.scatter(row,col)
plt.scatter(xo,yo,c='black')

finished=0
t=0
while finished==0:
    r1=np.random.randint(0,np.size(row)-1)
    posmat=[]
    pos_x=row[r1]
    pos_y=col[r1]
    stuck=0
    
    while stuck==0:
        pos_x_new,pos_y_new=randomwalk2d(grid_size, pos_x, pos_y)
        t=t+1
        bool1=np.any(grid1[pos_x_new-1:pos_x_new+1,pos_y_new-1:pos_y_new+1]==1)
        if bool1:
            grid1[pos_x_new,pos_y_new]=1
            if delta_x(pos_x_new,xo)**2 +delta_y(pos_y_new,yo)**2>=radius1**2:
                finished=1
            break;
            
        elif delta_x(pos_x_new,xo)**2 +delta_y(pos_y_new,yo)**2>=(radius1+tolerance*radius1)**2:
            r=np.random.randint(0,np.size(row)-1)
            pos_x=row[r]
            pos_y=col[r]
        else:
            pos_x=pos_x_new
            pos_y=pos_y_new
        posmat.append([pos_x_new,pos_y_new])
    plt.scatter(pos_x_new,pos_y_new,c='coral',marker="+")
    plt.figure()
    plt.plot(posmat[0],posmat[1])
    
    
   
time_elapsed=time.time()-t1
            
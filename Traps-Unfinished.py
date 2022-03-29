import numpy as np
from matplotlib import pyplot as plt 

grid_num=500
c=10**-2
trap_num=c*grid_num**2
traps_placed=0
occ=np.zeros([grid_num+1,grid_num+1])
nPart=1000
trapped_time=np.zeros([nPart,1])
tmax=5000
surv_mat=np.zeros([nPart,tmax])


while traps_placed<trap_num:
    pos_x_trap=np.random.randint(0,grid_num+1)
    pos_y_trap=np.random.randint(0,grid_num+1)
    if occ[pos_x_trap,pos_y_trap]==0:
        occ[pos_x_trap,pos_y_trap]=-1
        traps_placed=traps_placed+1

for part in range(nPart):
    
    #Place Particles
    pos_x=np.random.randint(0,grid_num+1)
    pos_y=np.random.randint(0,grid_num+1)
    t=0
    
    
    if occ[pos_x,pos_y]==-1:
        trapped=1
        trapped_time[part]=0
        surv_mat[part,t]=0
    else:
        trapped=0
        surv_mat[part,t]=1
    while trapped==0:
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
        if occ[pos_x,pos_y]==-1:
            trapped=1
            trapped_time[part]=t+1
            
            surv_mat[part,t]=0
            break
        else:
            surv_mat[part,t]=1
        
        
        t=t+1

plt.figure()    
plt.title('Histogram of Trapping Times')
plt.hist(trapped_time,bins='auto')
plt.grid()
plt.figure()
xs=np.linspace(0,np.size(surv_mat,axis=1),np.size(surv_mat,axis=1))
ys=np.sum(surv_mat,axis=0)
plt.scatter(xs,nPart-ys)
steps=np.linspace(10,1000,tmax)
s_theoretical_2d=np.pi*steps/np.log(steps)
phi=(1-c)*s_theoretical_2d
plt.plot(steps,phi)
        

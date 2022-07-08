import numpy as np
from matplotlib import pyplot as plt 

grid_num=500
c=10**-2
trap_num=c*grid_num**2
traps_placed=0
occ=np.zeros([grid_num+1,grid_num+1])
nPart=1000
trapped_time=np.zeros([nPart,1])




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

    else:
        trapped=0

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
            
            
            break
        t=t+1
        
tmax=int(np.max(trapped_time))
plt.figure()    
plt.title('Histogram of Trapping Times for c=0.01')
plt.grid()
plt.hist(trapped_time,bins='auto',alpha=0.6,density=True)
plt.ylabel("Trapping Times Probability")
plt.xlabel("Trapping time t")

trapped_time=np.sort(trapped_time,axis=0)
trapped_mat=[]
sum1=0
for i in range(0,tmax+1):
    for j in range(nPart):
        if trapped_time[j]==i:
            sum1=sum1+1
    trapped_mat.append((nPart-sum1)/nPart)

t1=np.linspace(0,tmax,tmax+1)
phi=pow((1-c),(np.pi*t1/np.log(8*t1)))
plt.figure()   
plt.title("Propability of Survival Phi - Trapping time t")
plt.ylabel("Propability of Survival Phi")
plt.xlabel("Trapping time t")
plt.grid()
plt.scatter(t1,trapped_mat,label='Simulated Data')  
plt.plot(t1,phi,label='Theoretical Distribution c=0.01',color='coral',linewidth=4)

plt.legend()  
       
grid_num=500
c=10**-3
trap_num=c*grid_num**2
traps_placed=0
occ=np.zeros([grid_num+1,grid_num+1])
nPart=1000
trapped_time=np.zeros([nPart,1])




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

    else:
        trapped=0

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
            
            
            break
        t=t+1
        
tmax=int(np.max(trapped_time))
plt.figure()    
plt.title('Histogram of Trapping Times for c=0.001')
plt.grid()
plt.ylabel("Trapping Times Probability")
plt.xlabel("Trapping time t")
plt.hist(trapped_time,bins='auto',alpha=0.6,density=True)


trapped_time=np.sort(trapped_time,axis=0)
trapped_mat=[]
sum1=0
for i in range(0,tmax+1):
    for j in range(nPart):
        if trapped_time[j]==i:
            sum1=sum1+1
    trapped_mat.append((nPart-sum1)/nPart)

t1=np.linspace(0,tmax,tmax+1)
phi=pow((1-c),(np.pi*t1/np.log(8*t1)))
plt.figure()   
plt.title("Propability of Survival Phi - Trapping time t")
plt.ylabel("Propability of Survival Phi")
plt.xlabel("Trapping time t (steps)")
plt.grid()
plt.scatter(t1,trapped_mat,label='Simulated Data')  
plt.plot(t1,phi,label='Theoretical Distribution c = 0.001',color='coral',linewidth=4,)
plt.legend() 
plt.figure()
plt.loglog(t1,phi) 
         

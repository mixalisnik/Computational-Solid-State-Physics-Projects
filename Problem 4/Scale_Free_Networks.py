import matplotlib.pyplot as plt
import numpy as np


np.random.seed(4408)
# def f1(y,ymin,gamma):
#     return 1/(1-gamma)*(y**(1-gamma)-ymin**(1-gamma))
N=10000
ymax1=9999
def f2(x,ymax,ymin,gamma):
    return ((ymax**(1-gamma)- ymin**(1-gamma))*x +ymin**(1-gamma))**(1/(1-gamma))
mat1=[]   
histdat=np.zeros(10000)
maxk=0
for i in range(100000):
    r=np.random.rand()
    r1=np.round(f2(r,ymax1,1,2.))
    mat1.append(r1)
    histdat[int(r1)]=histdat[int(r1)]+1
    if r1>maxk:
        maxk=r1
   
xx=np.arange(1,maxk+1,1)
plt.figure(0)
plt.scatter(np.log(xx[:int(maxk)]),np.log(histdat[:int(maxk)]),color='coral')

mat1=[]   
histdat=np.zeros(10000)
maxk=0
for i in range(100000):
    r=np.random.rand()
    r1=np.round(f2(r,ymax1,1,2.5))
    mat1.append(r1)
    histdat[int(r1)]=histdat[int(r1)]+1
    if r1>maxk:
        maxk=r1

xx=np.arange(1,maxk+1,1)
plt.figure(0)
plt.scatter(np.log(xx[:int(maxk)]),np.log(histdat[:int(maxk)]),color='blue')
    
    
mat1=[]   
histdat=np.zeros(10000)
maxk=0
for i in range(100000):
    r=np.random.rand()
    r1=np.round(f2(r,ymax1,1,3))
    mat1.append(r1)
    histdat[int(r1)]=histdat[int(r1)]+1
    if r1>maxk:
        maxk=r1
    
xx=np.arange(1,maxk+1,1)
plt.figure(0)
plt.scatter(np.log(xx[:int(maxk)]),np.log(histdat[:int(maxk)]),color='red')
plt.title("Coral: gamma = 2 Blue: gamma = 2.5 Red: gamma = 3")
plt.xlabel("log(k)")
plt.ylabel("log(P(k))")



import matplotlib.pyplot as plt
import numpy as np
np.random.seed(4408)
def f1(y,ymin,gamma):
    return 1/(1-gamma)*(y**(1-gamma)-ymin**(1-gamma))
def f2(x,ymax,ymin,gamma):
    return ((- ymin**(1-gamma))*x +ymin**(1-gamma))**(1/(1-gamma))
mat1=[]    
for i in range(100):
    r=np.random.rand()
    r1=f2(r,0,1,2.)
    mat1.append(r1)
plt.hist(mat1, density=True, label = "Numbers")
    
    
    


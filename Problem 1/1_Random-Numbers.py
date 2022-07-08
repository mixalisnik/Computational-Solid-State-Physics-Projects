import numpy as np
from matplotlib import pyplot as plt 

np.random.seed(4408)
N=[10,100,1000,10000,100000,1000000]
mean_mat=[]

for i in N:
    
    x=np.random.rand(i)
    mean_mat.append(np.mean(x))
    
    

plt.semilogx(N,mean_mat)
plt.title('Mean M of N Random Numbers - N ') #Set title of plot.
plt.ylabel(' M(N) ') #Set x and y labels
plt.xlabel('N')
plt.grid()
plt.show()
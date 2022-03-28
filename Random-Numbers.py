import numpy as np
from matplotlib import pyplot as plt 

np.random.seed(4408)
N=np.array([10,100,1000,10000,100000,1000000])
mean_mat=np.zeros([np.size(N),1])
j=0
for i in N:
    
    x=np.random.rand(i)
    mean_mat[j]=np.mean(x)
    
    j=j+1

plt.semilogx(N,mean_mat[:])
plt.title('Mean M of N Random Numbers - N ') #Set title of plot.
plt.ylabel(' M(N) ') #Set x and y labels
plt.xlabel('N')
plt.grid()
plt.show()
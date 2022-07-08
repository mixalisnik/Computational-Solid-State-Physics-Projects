import numpy as np
from matplotlib import pyplot as plt

x=np.array([[0,0],[0,1],[1,0],[1,1]]) #x array
GT=np.array([[0],[1],[1],[0]]) #ground truth array
outputs=np.zeros(np.size(x,axis=0)) #Output Matrix
error=np.zeros(np.size(x,axis=0)) #Error Matrix

num_epoch=10000 #Max Number of Epochs
n=0.2 #Learning Rate
tolerance=0.01 #Error tolerance
def u(x1,x2,w1,w2,b):
    return x1*w1+x2*w2+b

def sigmoid(u):
    return 1/(1+np.exp(-u))

def sigmoid_prime(u):
    return sigmoid(u)*(1-sigmoid(u))

def error_function(yn,d):
    return 0.5*(d-yn)**2

#Initialize random wi

w=np.random.rand(9)

for ep in range(num_epoch):
    
    for i in range(np.size(x,axis=0)):
    #Forward Propagation
        u3=u(x[i,0],x[i,1],w[1],w[2],w[5])
        y3=sigmoid(u3)
        
        u4=u(x[i,0],x[i,1],w[0],w[3],w[4])
        y4=sigmoid(u4)
        
        u5=u(y4,y3,w[7],w[6],w[8])
        output=sigmoid(u5)
        
        outputs[i]=output
        error[i]=error_function(output,GT[i])
       
    #Back Propagation
        
        d5=output*(1-output)*(GT[i]-output)
        d4=y4*(1-y4)*d5*w[7]
        d3=y3*(1-y3)*d5*w[6]
        d2=x[i,1]*(1-x[i,1])*(d3*w[2]+d4*w[3])
        d1=x[i,0]*(1-x[i,0])*(d3*w[1]+d4*w[0])
        
    #Change the weights
        dw0=n*d4*x[i,0]
        dw1=n*d3*x[i,0]
        dw2=n*d3*x[i,1]
        dw3=n*d4*x[i,1]
        dw4=n*d4
        dw5=n*d3
        dw6=n*d5*y3
        dw7=n*d5*y4
        dw8=n*d5
        dw=np.array([[dw0],[dw1],[dw2],[dw3],[dw4],[dw5],[dw6],[dw7],[dw8]])
        w[0]=w[0]+dw0
        w[1]=w[1]+dw1
        w[2]=w[2]+dw2
        w[3]=w[3]+dw3
        w[4]=w[4]+dw4
        w[5]=w[5]+dw5
        w[6]=w[6]+dw6
        w[7]=w[7]+dw7
        w[8]=w[8]+dw8
     #Calculate Error   
        
        error_sum=np.sum(error)
    print("Epoch: ",ep,"Error: ", error_sum)
 
    if error[0]<tolerance and error[1]<tolerance and error[2]<tolerance and error[3]<tolerance:
        print("Output of ANN is : ",outputs,"as expected")
        break;
print("Matrix of w is: ",w)
# Computational-Solid-State-Physics
## Problem 1
  
**Random Numbers**  
  

* Creates a computer program that derives the average from N random numbers obtained from a 
uniformly random distribution of numbers in space [0 to 1].   
  
* The program must run for N = 10, 100, 1000,
10000, 100000, 1000000 random numbers.   
  
* The graph of the mean as a function of N (where the N 
axis is logarithmic) is made.  

**Random Walk 1D and 2D**  

* Creates a program that performs a random walk for N = 1000 steps, in the case of systems of (a) 1 
dimension and (b) 2 dimensions.   
  
* The program must calculate the square of the displacement, R^2
.   
  
**Random Walk 1D and 2D with figure**  

* Runs the 
program for 10000 runs and finds the R^2 average.   

* Uses the previous program to determine <R^2>, but now every 100 steps, from 1 to 1000.   
  
* Finds the 
average for 10000 runs.   
  
* Makes a graph of the results.   
  
* Finds the optimal straight line using the least squares 
method.  
  
**Distribution of R**  

* Creates a program that performs a random walk for N = 1000 steps, in 1 dimension, just like in problem 2.  
  
* Calculates the position (R) located after the N steps, for 100000 runs.   
  
* Next, it prepares the distribution of 
the values of R.    
   
* Repeats the same for N = 2000 steps.  
  
* Makes a graph of the two distributions for the two 
values of N.  
  
**Unique Sited visited**  

* Creates a program in which a particle will perform a random walk for t = 1000 steps in a one-
dimensional, two-dimensional and three-dimensional system.    
  

* The program calculates the S
where S is the number of grid sites that the particle visited at least once.  
  
* 10000 simulations are run and 10 points are found (one every 100 steps, from 0 to 1000), which will be the average of 10000 simulations. 
The graph of  S as a function of time t is made.  
  
* Plots and compares to the analytical theoretical results.  
  
**Traps**
* Creates a program in which there is a 2D grid with a size of 500x500.  
  
* In this grid, a 
number of traps is randomly  of concentration c is randomly entered.  
* Then 1 particle is placed in a random position in the 
grid and the particle is allowed to perform a random walk.  
  

* The walk will stop when the particle happens to fall 
into a trap as it moves.  
  

* The time that it took for the particle to be trapped is t.  
  

* 100000 simulations are run and the trapping times are monitored.  
  
* The distribution of those times is made.  
  
* When the particle reaches the ends of the grid, it should not be allowed to leave the grid, but 
remain inside by reflecting on the walls of the grid.  
  

* Calculates the probability of survival Φ (t), that is the percentage 
of particles that had not fallen into a trap after t steps and 
compare the results with Rosenstock's theoretical approach, for which:
Φ (t) = (1- c) <S (t)> where Φ (t) is the probability of survival and <S (t)> the average number of lattice 
positions that particle visited at least once.  



## Problem 2
This model was proposed in the published paper
T.A.Witten, L.M.Sander, “Diffusion-Limited Aggregation, a Kinetic Critical Phenomenon”, Physical Review 
Letters vol 47, no 19, 1981.  
  
A Diffusion Limited Aggregate structure is created and it's fractal dimensionality is
calculated.  

Consider a square grid of 2 dimensions of size 450 x 450 and place a particle in the center.  

Then create a circle with a radius of 200, centered in the square grid.   
  
Then select a new particle and place 
it randomly at a point on the periphery of the circle.   
  

The new particle performs a random walk until one 
of the following possibilities occurs: 
   
(a) occupies a position "next" to the central particle, on either side of 
it   
  
(b) it leaves far enough away from the original area (exits the grid).   
  
In case (a) this particle is attached 
to the original particle, its path stops, and so now there is an aggregation of two particles.   
  
In case (b) the 
particle should not leave the grid but it should be repositioned at the periphery of the circle at another 
random point, and continue its random walk.   
  
The process is repeated for a third, fourth particle, etc. and 
continues for as many particles as needed until the growing aggregate from the center of the circle 
touches its circumference.  
  
Sketch the state of the system at the end of the process.  
  
Determine the fractal dimension of the structure you created using the following method:   
  
First, select a 
position in the grid randomly at a maximum distance of 10 grid sites from the center of the circle.   
This 
position now becomes the center of a square with side L = 10.   
  
You count the number of sites M that are 
occupied by particles in this square that has dimensions 10x10.  
  
Then increase L by 10 and create a new 
square with the same center and side L = 20.   
  
Now calculate the new M.   
  
Continue the process by enlarging 
the side of the square, so that you finally have 10 such squares with the last one having side L = 100.   
  
Make 
the graph of L as a function of M.   
  
If this structure is fractal then the number of occupied positions M 
follows a relation of the form M ~ L^df, with df being the fractal dimension of this structure.   
  
Therefore, by 
depicting in a log-log diagram the quantity M for the various values of L, we find the df from the slope.  
  
We 
must make N runs of the process and obtain their mean.   
  
So we repeat this process N = 20 times, we keep 
the values of M for the N repetitions and we calculate the average of the 10 values of M.   
  
Finally, we find 
the dimension df in the above way.


## Problem 3
The percolation problem is studied.  
  
A grid of particles is created, with probability p for a grid point to be filled.  
  
The CMLT algorithm is applied and the full distribution of clusters is found for different p values. 
  
The critical point pc is computed through the simulation. 
  
The average size of clusters is computed for different values of p.  
  
The average size of clusters without the largest cluster is also computed for different p values.  
  
The largest cluster size is computed for different p values as well.  


## Problem 4
### Erdos Renyi Network  

An Erdos-Renyi network with N = 10000 nodes is created.   
  
It is a network in which each of the N nodes 
has a random number of k connections.   
  
The rule that between two nodes there is a probability 
p = 1/6 that there is a connection is applied.  
  
The number of k connections of each node is found and a plot of the distribution of k, P (k), as a function of k is made.  
  
The 
mean value of k is calculated.  
### Small World Network  

A Small World Network with N = 1000 nodes is created.   
  
Initially each node has exactly k=14
connections, i.e. there is a total of 14x1000=15000 connections.   
  
The connections are redistributed
with probability p = 0.20.   
  
The plot of the distribution of k, P (k), as a function of k is created. 

### Power Law Network  
A power law network (scale-free network) with N = 10000 nodes and γ=3 is created.   
  
A random 
number of k connections for each node is generated with probability P(k)=k^-γ.   
  
The graph of the distribution of k, 
P (k), as a function of k is plotted.


## Problem 5
An artificial neural network (ANN) is created to solve the X-OR problem, using the back-propagation method.   
  
The input level consists of 2 nodes, the hidden level also consists of 2 nodes and the output level consists 
of one node.   
  
The initial weights of the links are randomly selected from a uniform 
distribution w ∈ (-1.1).   
  
The maximum acceptable error in the output (1/2|output-target|\^2
) is considered to be 0.01 and the learning rate η = 0.2.  
  

The maximum number of training cycles (epochs) is 10000.

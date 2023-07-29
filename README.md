# Downhill Simplex - MicroPython
 Python implementation on 2D Downhill Simplex / Nelder Mead Optimization to run on MicroPython and ESP32 platform, requires no external libraries.


```
optimize(objfunc, u, v, w,xmin=0,ymin=0, xmax=1000, ymax=1000, tol=4e-5)
```

### arguments
<ul>
<li>objfunc is the function you want to minimize, it should output a scalar, and take two arguments as inputs, which we refer to as x and y</li>
<li>u, v, and w are Point objects with x and y coordinates, that form the initial simplex (triangle). This class is defined in classes.py.</li>
<li>xmin and ymin are the minimum values that the objective function will evaluate</li>
<li>xmax and ymax are the maximum values that the objective function will evaluate</li>
<li>tol is the tolerance of the convergence step of the algorithm, if the standard deviation of the three points in the initial simplex is less than or equal to the tolerance, the optimization terminates, and returns the coordinates of the best-performing point</li>
 </ul>

### output
The coordinates of the best performing point
 

## Usage
```
def objective_function(x,y):
    # write your 3d scalar function here
    return value

u = Point(20,20)
v = Point(50,50)
w = Point(0,0)

optimize(objective_function,u,v,w)
```

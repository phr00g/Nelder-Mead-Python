# Downhill Simplex - MicroPython
 testing and writing manual implementation on 2D Downhill Simplex / Nelder Mead Optimization to run on MicroPython and ESP32 platform, requires not external libraries

 ## Usage
```
optimize(objfunc, u, v, w, xmax=1000, ymax=1000, tol=4e-5, iterations=0)
```
Where objfunc is the function you would like to minimize, u, v, and w are Point objects that have x and y coordinates. This class is defined in classes.py
For example: 
> u = Point(300,200)

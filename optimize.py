'''
Main Optmization Loop
'''

# note: objective function is get_rssi(x,y)
import math
from matrix_maker import matrix
from classes import * 



#optimization loop, break to exit

while True:


    #step 0 - initialize
    #enter coordinates for three intial simplex points
    #determine what value to compare point std dev to for optimization termination in step 6
    #other stuff


    #step 1 - sort - unconditional
    #order points so that w u is best, v is middle, and w is worst


    #step 2 - reflect - unconditional
    #reflect worst point w through centroid of remaining points to obtain reflected point r
    #eval get_rssi(r)
    #if r better than v, but not u, then assign w = r and go to step 6



    #step 3 - extend - if r better than u
    #find extended point e
    #if e better than r , assign w = e  and go to step 6
    #if e worse than r, assign w = r and go to step 6

    #step 4 - contract if jump to step 6 conditions are not met in previous two steps
    #find ci and co, ci is 1/4 way between w and r, co is 3/4
    #determine better point between ci and co
    #if either point is better than v, assign the better point w = v and go to tep 6
    #if not, go to step 5

    #step 5 - shrink - if all previous conditions to jump to step 6, fail   
    #calc vprime and wprime
    #vprime is centriod between u and v
    #wprime is centroid between u and w
    #assign v = vprime and w = wprime
    #go to step 6

    #step 6 - convergence
    #Check if optimization should end / conditions are satisfied
    #sample std dev of u,v,w is less than tolerance ---> return coords of u,v,w and break







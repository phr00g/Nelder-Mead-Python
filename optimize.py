'''
Main Optmization Loop
'''

# note: objective function is get_rssi(x,y)
import math
from matrix_maker import matrix , get_rssi
from classes import * 



#for now, u v and w must be point objects
def optimize(objfunc,u,v,w,xmax = 1000,ymax = 1000,tol = 4e-5):



    #shorthand for calling objective function on point
    def f(point):
        return objfunc(point.x,point.y)
    

    def order(u,v,w):#order points so that w u is best, v is middle, and w is worst, returns them: u,v,w
        
        #if w performs better
        if objfunc(w.x,w.y) < objfunc(v.x,v.y):
            #copy v
            vtemp = v.copy()
            #swap v and w
            v = w.copy()
            w = vtemp.copy()
        #if w is better than u swap them
        if objfunc(w.x,w.y) < objfunc(u.x,u.y):
            utemp = u.copy()
            u = w.copy()
            w = utemp.copy()
        #if v better than u, swap them
        if objfunc(v.x,v.y) < objfunc(u.x,u.y):
            vtemp = v.copy()
            v = u.copy()
            u = vtemp.copy()
        return u,v,w
    
    #if sample std dev of values of points is leq tolerance, return True, else return false
    def convergence(u,v,w):
        fu = f(u)
        fv = f(v)
        fw = f(w)
        fs = [fu,fv,fw]
        avg = (fu + fv + fw)/3
        total = sum([(i-avg)**2 for i in fs])
        std = math.sqrt(total/2) #std dev of obj function values
        if std <= tol:
            return True
        else:
            return False
        
    def constrain(point):
        if point.x > xmax:
            point.x = xmax -1
        if point.y > ymax:
            point.y = ymax -1
        if point.x < 0:
            point.x = 0
        if point.y < 0:
            point.y = 0
        return point

        
#######################################################################################        
       
    while True:


        #step 1 - sort - unconditional
        u,v,w = order(u,v,w)
        #they are now ordered
       
        #step 2 - reflect - unconditional
        #reflect worst point w through centroid of remaining points to obtain reflected point r
        #eval get_rssi(r)
        #if r better than v, but not u, then assign w = r and go to step 6
        
        #get reflected point r
        r = reflect(u,v,w)
        r = constrain(r)
        
        #if r is better than v but worse than u, assign w = r
        if f(r) < f(v) and f(r) >= f(u):
            w = r.copy()
            #if convergence condition is met, return best point, else restart at step 1
            if convergence(u,v,w):
                #find best point and then return best point
                u,v,w = order(u,v,w)
                return (u.x,u.y)
            else:
                continue

        #step 3 - extend - if r better than u
        #find extended point e
        #if e better than r , assign w = e  and go to step 6
        #if e worse than r, assign w = r and go to step 6

        if f(r) < f(u):
            e = extend(u,v,w)
            e = constrain(e)

            if f(r) > f(e):
                w = e.copy()
                if convergence(u,v,w):
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    return (u.x,u.y)
                else:
                    continue
            
            if f(r) < f(e):
                w = r.copy()
                if convergence(u,v,w):
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    return (u.x,u.y)
                else:
                    continue








        #step 4 - contract if jump to step 6 conditions are not met in previous two steps
        #find ci and co, ci is 1/4 way between w and r, co is 3/4
        #determine better point between ci and co
        #if either point is better than v, assign the better point w = better pointand go to tep 6
        #if not, go to step 5


        ci,co =contract(w,r)

        if f(ci) < f(co) and f(ci) < f(v):
            w = ci.copy()
            
            if convergence(u,v,w):
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    return (u.x,u.y)
            else:
                continue

        elif f(co) < f(ci) and f(co) < f(v):
            w = co.copy()
            if convergence(u,v,w):
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    return (u.x,u.y)
            else:
                continue

        



        #step 5 - shrink - if all previous conditions to jump to step 6, fail   
        #calc vprime and wprime
        #vprime is centriod between u and v
        #wprime is centroid between u and w
        #assign v = vprime and w = wprime
        #go to step 6

        vprime,wprime = shrink(u,v,w)
        v = vprime.copy()
        w = wprime.copy()

        if convergence(u,v,w):
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    return (u.x,u.y)
        else:
            continue


p1 = Point(100,200)
p2 = Point(200,300)

p3 = Point(700,700)
        
print("Best found point at: " , optimize(get_rssi,p1,p2,p3))






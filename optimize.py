'''
Main Optmization Loop
'''

# note: objective function is get_rssi(x,y)
import math

from classes import * 






#for now, u v and w must be point objects
def optimize(objfunc,u,v,w,xmin = 0,ymin=0,xmax = 1000,ymax = 1000,tol = 15):
    
     #shorthand for calling objective function on point
    def f(point):
        return objfunc(point.x,point.y)
    

    def order(u,v,w):#order points so that w u is best, v is middle, and w is worst, returns them: u,v,w    
        print("Ordering: going to points of initial simplex" )
        print("evaluating w  with x,y:  {},{} ".format(w.x,w.y))
        wval = objfunc(w.x,w.y)
        print("evaluating v with x,y: {},{}:  ".format(v.x,v.y))
        vval = objfunc(v.x,v.y)
        print("evaluating u with x,y {},{} ".format(u.x,u.y))
        uval = objfunc(u.x,u.y)
        
        
        
        
        #if u is best
        if uval < wval and uval < vval:
            #and v better than w
            if vval < wval:
                return u,v,w
            else:
                return u,w,v
        #if v is best
        if vval < uval and vval < wval:
            #and u better than w
            if uval < wval:
                return v,u,w
            else:
                return v,w,u
        #if w is best
        else:
            #and u better than v
            if uval < vval:
                return w,u,v
            else:
                return w,v,u
    
        #if w is better than u swap them
        if wval < uval :
            utemp = u.copy()
            u = w.copy()
            w = utemp.copy()
            
            
        



   
    
    #if sample std dev of values of points is leq tolerance, return True, else return false
    def convergence(u,v,w):
        print("Step 6: Convergence")
        print("Finding RSSI at point U")
        fu = f(u)
        print("Finding RSSI at point V")
        fv = f(v)
        print("Finding RSSI at point W")
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
        if point.x < xmin:
            point.x = xmin
        if point.y < ymin:
            point.y = ymin
        return point

        
#######################################################################################        
       
    while True:

        
        #step 1 - sort - unconditional
        print("Step 1: ordering u,v,w")
        u,v,w = order(u,v,w)
        #they are now ordered
        print("The x,y vals of u,v,w are: u = ({},{}) , v = ({},{}) , w=({},{})".format(u.x,u.y,v.x,v.y,w.x,w.y))
       
        #step 2 - reflect - unconditional
        #reflect worst point w through centroid of remaining points to obtain reflected point r
        #eval get_rssi(r)
        #if r better than v, but not u, then assign w = r and go to step 6
        
        #get reflected point r
        print("Step 2: Reflecting................")
        r = reflect(u,v,w)
        print("Reflected point R = {},{}".format(r.x,r.y))
        r = constrain(r)
        print("R after being constrained is = {},{}".format(r.x,r.y))
        
        print("Finding RSSI val at point r.....")
        fr = f(r)
        print("Finding RSSI val at point v.....")
        
        fv = f(v)
        print("Finding RSSI val at point u.....")
        
        fu = f(u)
        
        #if r is better than v but worse than u, assign w = r
        if fr < fv and fr >= fu:
            print("R is better than V but worse than U, testing for convergence and ending or restarting")
            w = r.copy()
            #if convergence condition is met, return best point, else restart at step 1
            if convergence(u,v,w):
                print("convergence is true, terminating program")
                #find best point and then return best point
                u,v,w = order(u,v,w)
                print("Best point found at ({},{})".format(u.x,u.y))
                return (u.x,u.y)
            else:
                print("convergence not true, going to step 1")
                continue 

        #step 3 - extend - if r better than u
        #find extended point e
        #if e better than r , assign w = e  and go to step 6
        #if e worse than r, assign w = r and go to step 6
        print("Step 3: extending")
        if fr < fu:
            print("R is better than U, calculating extended point E")
            e = extend(u,v,w)
            print("Point E has x,y {},{}".format(e.x,e.y))
            e = constrain(e)
            print("After being constrained ,Point E has x,y {},{}".format(e.x,e.y))
            print("Evaluating RSSI at point E........")
            fe = f(e)

            if fr > fe:
                print("E is better than R , assigning W = E, and checking convergence")
                w = e.copy()
                if convergence(u,v,w):
                    print("Convergence is true, program terminating")
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    print("Best point found at ({},{})".format(u.x,u.y))
                    return (u.x,u.y)
                else:
                    print("Convergence is false, going to step 1")
                    continue
            
            if fr < fe:
                print("R is better than E, assigning W = R and checking convergence")
                w = r.copy()
                if convergence(u,v,w):
                    print("Convergence is true, terminating program")
                #find best point and then return best point
                    u,v,w = order(u,v,w)
                    print("The best x location is : {}, and the best y location is {}".format(u.x,u.y))
                    return (u.x,u.y)
                else:
                    print("Convergence is false, going to step 1")
                    continue








        #step 4 - contract if jump to step 6 conditions are not met in previous two steps
        #find ci and co, ci is 1/4 way between w and r, co is 3/4
        #determine better point between ci and co
        #if either point is better than v, assign the better point w = better pointand go to tep 6
        #if not, go to step 5
        
        print("Step 4: contracting")
        print("calculating points CI, CO")
        ci,co =contract(w,r)
        print("Finding RSSI at point CI...........")
        fci = f(ci)
        print("Finding RSSI at point CO...........")
        fco = f(co)
        print("Finding RSSI at point V...........")
        fv = f(v)

        if fci < fco and fci < fv:
            print("CI is better than CO and V , assigning W = CI and checking for convergence.")
            w = ci.copy()
            
            if convergence(u,v,w):
                print("Convergence is true, terminating..")
                #find best point and then return best point
                u,v,w = order(u,v,w)
                print("Best point found at ({},{})".format(u.x,u.y))
                return (u.x,u.y)
            else:
                print("Convergence is false, going to step 1")
                continue

        elif fco < fci and fco < fv:
            print("CO is better than CI and V, assigning W = CO and checking for convergence..")
            w = co.copy()
            if convergence(u,v,w):
                print("Convergence is true, terminating")
                #find best point and then return best point
                u,v,w = order(u,v,w)
                print("Best point found at ({},{})".format(u.x,u.y))
                return (u.x,u.y)
            else:
                print("Convergence is false, going to step 1 ...")
                continue

        



        #step 5 - shrink - if all previous conditions to jump to step 6, fail   
        #calc vprime and wprime
        #vprime is centriod between u and v
        #wprime is centroid between u and w
        #assign v = vprime and w = wprime
        #go to step 6
        
        print("Step 5: Shrinking")
        print("Calculating vprime and wprime......")
        vprime,wprime = shrink(u,v,w)
        print("vprime has x,y of ({},{}) and wprime has x,y of ({},{})".format(vprime.x,vprime.y,wprime.x,wprime.y))
        print("Assigning v = vprime and w = wprime....")
        v = vprime.copy()
        w = wprime.copy()

        print("Step 6: Checking Convergence")
        if convergence(u,v,w):
            print("Convergence is true, terminating")
                #find best point and then return best point
            u,v,w = order(u,v,w)
            print("Best point found at ({},{})".format(u.x,u.y))
            return (u.x,u.y)
        else:
            print("Convergence is false, going to step 1")
            continue









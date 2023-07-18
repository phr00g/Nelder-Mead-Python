### Holds all classes and related methods for operations on points and vectors required for downhill simplex optimization
from matrix_maker import matrix
class Point():
    pointz = []
    def __init__(self,x,y):
        self.x = x
        self.y = y #lol lol ol 

        Point.pointz.append(self)

    def copy(self):
        return Point(self.x,self.y)
    
    def rssi(self):

        #multiply by negative one because we are using minimization algorithm, but we are trying to maximize
        return -1 * matrix[round(self.y)][round(self.x)]
    


def difference(p1,p2):#not commutative
    difx = p1.x - p2.x
    dify = p1.y - p2.y
    return Point(difx,dify)

def add(p1,p2): #commutative
    return Point(p1.x + p2.x,p1.y + p2.y)


def scale(point,some_constant):
    sx = point.x * some_constant
    sy = point.y * some_constant
    return Point(sx,sy)


def centroid(p1,p2):

    xcent = (p1.x + p2.x) / 2
    ycent = (p1.y + p2.y) / 2
    return Point(xcent,ycent)

def reflect(p1,p2,p3): #p1 and p2 are not moving, p3 is
    cent = centroid(p1,p2)
    diff = difference(cent,p3) #vec / point from p3 to centroid, must add to centroid to get reflection

    return add(cent,diff)

def extend(p1,p2,p3): #returns point e
    cent = centroid(p1,p2)
    diff = difference(cent,p3)
    extdiffx = diff.x * 2
    extdiffy = diff.y * 2
    extdiff = Point(extdiffx,extdiffy)
    return add(extdiff,cent)
    
def contract(w,r):

    diff = difference(r,w)

    sc1 = scale(diff,1/4)
    sc2 = scale(diff,3/4)

    c1 = add(w,sc1)
    c2 = add(w,sc2)

    return c1,c2
    

def shrink(u,v,w):
    
    vprime = centroid(u,v)
    wprime = centroid(u,w)
    return vprime,wprime




## The code solves the Brachistochrone problem 
## http://mathworld.wolfram.com/BrachistochroneProblem.html
## By approximating integrals. 


import random
from random import randint
from math import cos, sin, radians, sqrt
import matplotlib.pyplot as plt

g = 9.8
s = sqrt(2)/99

setOfPoints = [[0], [1]]
velAtPoint = [0]


def setPoints():
    for p in range(0, 98):
        theta = radians(randint(-90, 1))
        setOfPoints[0].append(setOfPoints[0][p] + s * cos(theta))
        setOfPoints[1].append(setOfPoints[1][p] + s * sin(theta))
    setOfPoints[0].append(1)
    setOfPoints[1].append(0)
    return setOfPoints

# def s(p)
#     return ((setOfPoints[p][0] - setOfPoints[p-1][0])**2+(setOfPoints[p][1] - setOfPoints[p-1][1])**2)**0.5
    
# for p in range(1, len(setOfPoints)):
#     velAtPoint.append((2 * g * s(p) + velAtPoint[p-1]**2)**0.5)
    


#2gs = v^2 - u^2
#sqrt(2gs+u^2) = v


#dv = ds/dt
#dv dt = ds
#dt = ds/dv

#T = integral from 0,0 to 1,1 ds/dv  
def linIntegrate():
    T = 0
    for v in range(1, len(velAtPoint)):
        T += s(v) / velAtPoint[v]
    return T

#print(linIntegrate())
print(setPoints())
plt.plot(setOfPoints[0], setOfPoints[1], '-o')
plt.axis([0, 10, 0, 10])
plt.show()

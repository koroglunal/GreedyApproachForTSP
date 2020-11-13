import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
plt.style.use("bmh")

def GreedApproachTSP(coordinate):
    
    num_cities = len(coordinate)
    
    x = coordinate[:,0]
    y = coordinate[:,1]
    
    d = np.zeros(num_cities*num_cities).reshape(num_cities,num_cities)
    for  i in range(num_cities):
        for j in range(num_cities):
            d[i][j]=distance.euclidean(coordinate[i], coordinate[j])
            if  i==j:
                d[i][j]=999999
    
    D = np.copy(d)
    
    travel    = np.arange(1,num_cities)
    route     = [0]
    cost      = 0
    location  = 0
    while len(travel) != 1:
        to            = D[location].argmin()
        cost         += D[location][to]
        route.append(to)
        D[:,location] = np.ones(num_cities)*999999
        index         = np.where(travel==to)[0][0]
        travel        = np.delete(travel,index)
        location      = to
        
    route.append(travel[0])
    cost = cost + d[0][route[len(route)-1]]
    route.append(0)
    
    print("Route   :",route)
    print("Distance:",cost)
    
    plt.scatter(x,y)
    plt.title("TSA Solution with Greedy Approach")
    plt.plot(x[route],y[route])
    plt.show()
    

eurodist = np.array([[ 2290.27468 ,  1798.80293 ],
       [ -825.38279 ,   546.81148 ],
       [   59.183341,  -367.08135 ],
       [  -82.845973,  -429.91466 ],
       [ -352.499435,  -290.90843 ],
       [  293.689633,  -405.31194 ],
       [  681.931545, -1108.64478 ],
       [   -9.423364,   240.406   ],
       [-2048.449113,   642.45854 ],
       [  561.10897 ,  -773.36929 ],
       [  164.921799,  -549.36704 ],
       [-1935.040811,    49.12514 ],
       [ -226.423236,   187.08779 ],
       [-1423.353697,   305.87513 ],
       [ -299.49871 ,   388.80726 ],
       [  260.878046,   416.67381 ],
       [  587.675679,    81.18224 ],
       [ -156.836257,  -211.13911 ],
       [  709.413282,  1109.36665 ],
       [  839.445911, -1836.79055 ],
       [  911.2305  ,   205.9302  ]])

GreedApproachTSP(eurodist)

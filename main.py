
import math
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
#from random import random
dstPower = 2
inf = sys.maxsize
evaporation_factor = 0.02
pheromone_pow= 4
pheromone_trail = [[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]
,
[100, 100, 100, 100, 100, 100, 100, 100, 100]]
x = [[inf, 14, 12, 94, 45, 86, 53, 13, 20],
                        [14, inf, 77, 58, 52, 7, 23, 26, 42],
                        [12, 77, inf, 10, 13, 59, 35, 26, 97],
[94, 58, 10, inf, 71, 47, 49, 29, 35],
[45, 52, 13, 71, inf, 35, 23, 16, 4],
[86, 7, 59, 47, 35, inf, 68, 15, 23],
[53, 23, 35, 49, 23, 68, inf, 3, 44],
[13, 26, 26, 29, 16, 15, 3, inf, 55],
[20, 42, 97, 35, 4, 23, 44, 55, inf]]

    #[[10,10,10,10],[10,10,10,10],[10,10,10,10],[10,10,10,10],]


class Ant:
    def __init__(self, start, distances):
        self.distances = distances
            # [[10, 2, 3, 5],
            #              [8, 10, 9, 80],
            #              [6, 7, 10, 1],
            #              [4, 5, 9, 10]]
        self.route = []
        self.total_dst = 0
        self.start = start
        self.current = start
        self.visited = [start]

    def calc_desirability(self, flag):
        dsts = self.distances[self.current]
        desirabilities = []
        #print(self.visited)
        for dst in dsts:
            tempNode = self.distances[self.current].index(dst)
            if tempNode not in self.visited:
                pheromoneStrength = pheromone_trail[self.current][tempNode]
                if flag:
                    desirability = pow(1 / dst, dstPower)*pow(pheromoneStrength, pheromone_pow)
                else:
                    desirability = pow(1 / dst, dstPower)
                desirabilities.append(desirability)
            else:
                desirabilities.append(0)
        #print(desirabilities)
        return desirabilities


    def nextNode(self, flag):
        desirabilities = self.calc_desirability(flag)
        nextnodels = random.choices(self.distances[self.current], weights=desirabilities)
        #print(nextnodels)
        nextnode = self.distances[self.current].index(nextnodels[0])
        pheromone_trail[self.current][nextnode] += 1
        pheromone_trail[nextnode][self.current] += 1
        self.visited.append(nextnode)
        return nextnode

    def anTrail(self, flag=1):
        self.route.append(self.start)
        #print(self.distances[0])
        while len(self.route)<len(self.distances[0]):
            self.current = self.nextNode(flag)
            self.route.append(self.current)
            for i in range(len(pheromone_trail)):
                for j in range(0,n):
                    if pheromone_trail[i][j] > 0:
                        pheromone_trail[i][j]-=pheromone_trail[i][j]*evaporation_factor
                        pheromone_trail[j][i] -= pheromone_trail[j][i] * evaporation_factor
                # print(pheromone_trail)
                # print(self.route)
        self.route.append(self.start)
        print(self.route)
        return self.route



if __name__ == '__main__':
    #n = int(input())
    n = 9
    points = []
    x = np.random.rand(n)*20
    y = np.random.rand(n)*20
    #plt.scatter(x, y, c= 'black', s = 10)
    # print(x)
    # print(y)
    pheromone_trail =[]
    pheromones = []
    for i in range(0, n):
        for j in range(0, n):
            pheromones.append(7)
        pheromone_trail.append(pheromones)
        pheromones = []

    for i in range(0, n):
        points.append([x[i], y[i]])
   # print(points)
    for i in points:
        plt.scatter(i[0], i[1], c='black', s=10)
    distances =[]
    distance = []
    for i in points:
        for j in points:
            if set(i)== set(j):
                dst = inf
            else:
                dst = math.dist(i, j)
            distance.append(round(dst))
        distances.append(distance)
        distance = []
    print(points)
    a1 = Ant(0, distances)
    a2 = Ant(2, distances)
    a3 = Ant(1, distances)
    a4 = Ant(7, distances)
    r1 = a1.anTrail()
    for i in range(len(r1)-1):
        x_val = [points[r1[i]][0], points[r1[i+1]][0]]
        y_val = [points[r1[i]][1], points[r1[i + 1]][1]]
        plt.plot(x_val, y_val, 'bo', linestyle="--", linewidth = 2.5)
    r2 = a2.anTrail()
    for i in range(len(r2)-1):
        x_val = [points[r2[i]][0], points[r2[i+1]][0]]
        y_val = [points[r2[i]][1], points[r2[i + 1]][1]]
        plt.plot(x_val, y_val, color = 'red', linestyle="--", linewidth = 2)
    #plt.show()
    r3 = a3.anTrail()
    for i in range(len(r3)-1):
        x_val = [points[r3[i]][0], points[r3[i+1]][0]]
        y_val = [points[r3[i]][1], points[r3[i + 1]][1]]
        plt.plot(x_val, y_val, color = 'yellow', linestyle="--", linewidth = 1.5)
    #plt.show()
    r4 = a4.anTrail()
    for i in range(len(r4)-1):
        x_val = [points[r4[i]][0], points[r4[i+1]][0]]
        y_val = [points[r4[i]][1], points[r4[i + 1]][1]]
        plt.plot(x_val, y_val, 'black', linestyle="--", linewidth = 1)

    for i in pheromone_trail:
        print([round(x) for x in i])
    plt.show()
    max = 4
    count =0
    xval =[]
    yval =[]



    #plt.show()
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # ls = []
    # ls2 = []
    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         if i==j:
    #             ls.append("inf")
    #         else:
    #             ls.append(round(random()*(97)+3))
    #     ls2.append(ls)
    #     ls=[]
    #
    # for i in range(len(ls2)):
    #     for j in range(len(ls2)):
    #         ls2[i][j] = ls2[j][i]
    # for i in ls2:
    #     print(i)
    #print(ls2)

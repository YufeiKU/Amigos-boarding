import Ordering
import random
import numpy
import Airline3
import math

def run(method,filename):
    bigtime=[]
    k = 0.2
    while k <= 1:
        timelist=[]
        for i in range(20):
            seatlist=Ordering.ordering(30,6,4,method)

            speedlist=list(numpy.random.normal(1+k,.3,len(seatlist)))

            numbags=int(math.ceil(len(seatlist)*0.8))
            blist=list(numpy.random.normal(12,2,numbags))+[0 for i in range(len(seatlist)-numbags)]
            random.shuffle(blist)

            t=Airline3.board(seatlist,.5,.7,6,1,speedlist,blist)
            timelist.append(t)
        bigtime.append(timelist)
        k = k + 0.2

    numpy.savetxt(filename, bigtime, delimiter=',')

         

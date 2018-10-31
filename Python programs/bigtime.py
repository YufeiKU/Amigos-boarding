import Ordering
import random
import numpy
import Airline3
import math
from random import randrange, sample
def random_insert(lst, item):
    lst.insert(randrange(len(lst)+1), item)
    return lst
def run(method,filename):
    bigtime=[]
    for lp in range(10):
        timelist=[]
        for i in range(20):
            seatlist=Ordering.ordering(30,6,3,method)

            if lp*10>0:
                wo=int(math.ceil(lp*10/100*len(seatlist)))
                woList=[]
                for i in range(wo):
                    woList.append(seatlist.pop(random.randint(0,len(seatlist)-1)))
                for i in range(wo):
                    seatlist=random_insert(seatlist,woList[i])
                    
            numbags=int(math.ceil(len(seatlist)*80/100))
            blist=list(numpy.random.normal(12,2,numbags))+[0 for i in range(len(seatlist)-numbags)]
            random.shuffle(blist)


            speedlist=list(numpy.random.normal(1.5,.3,len(seatlist)))
            random.shuffle(blist)

            t=Airline3.board(seatlist,.5,.7,6,1,speedlist,blist)
            timelist.append(t)
        bigtime.append(timelist)

    numpy.savetxt(filename, bigtime, delimiter=',')

        

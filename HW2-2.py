import random
import time
import math
import numpy as np

def experiment(times, sides):
    t1=time.clock()
    dice = len(sides)
    print('==========================')
    print('Dice number =',dice)
    print('Sides =',sides)
    sum_num = sum(sides)
    value_num = np.linspace(dice,sum_num,sum_num-dice+1)
    list1 = np.zeros(sum_num-dice+1)
    for i in range(times):
	    Z = 0
	    for j in sides:
		    Z += random.randint(1,j)
		
	    list1[Z-dice] += 1

          
	    

    list1 /= times

    for i in range(len(list1)):
            print('[sides = {V}, Probability = {L}]'.format(V = int(value_num[i]), L = list1[i]))
    t2=time.clock()
    Elapsed_time = t2-t1
    print("Elapsed time =", t2-t1)


experiment(10000,[4,6])
experiment(10000,[5,10,15])
experiment(10000,[9,18,27])

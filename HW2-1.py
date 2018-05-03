import random
import time
import math
import numpy as np

def experiment(die_number, sides,times):
    print("==============================")
    print("Number of dies", die_number)
    print("Number of sides", sides)
    print("Number of trials = ", times)
    t1=time.clock()

    D=die_number
    S=sides
    T=times

    
    Z = np.linspace(1,S,S)
    A = np.zeros(T)
    for i in range(T):
	    for j in range(D):
		    A[i] += random.randint(1,S)
    print (Z)
    mean = D * sum(Z/S)
    variance = D * (sum(Z*Z/S) - sum(Z/S)*sum(Z/S))

    print("mean =", mean)
    print("variance =", variance)
    print("standard deviation =", variance**0.5)



    t2=time.clock()
    print("Elapsed time =", t2-t1)

    
    theory_mean = sum(A)/T
    theory_var = sum(pow((A-theory_mean),2))/T
    theory_std = pow(theory_var,0.5)
    
    print("theory mean value = ", theory_mean)
    print("theory varance value = ", theory_var)
    print("theory standard deviaction = ", theory_std)


    error_mean = abs(mean - theory_mean)/theory_mean
    error_var = abs(variance - theory_var)/theory_var
    error_std = abs(variance**0.5 - theory_std)/theory_std

    print("error theory mean value = ", error_mean*100,"%")
    print("error theory varance value = ", error_var*100,"%")
    print("error theory standard deviaction = ", error_std*100,"%")
    

experiment(2,10,10000)
experiment(10,20,10000)

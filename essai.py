
import math
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
from random import randrange
from matplotlib import pyplot

x=[0]
N = int(input("number of steps : "))
murdroite = 5
murgauche = -5

p=(len(x)//2*N)

def absorbing(xn, murdroite, murgauche):
    xmaxlife=1
    i=0
    while xmaxlife != 0 :
        if xn>murdroite :
            xn=murdroite
            xmaxlife==0
            print("xmaxlife = 0")
        if xn<murgauche :
            xn=murgauche
            xmaxlife == 0
            print("xmaxlife = 0")
        return(xmaxlife)


for i in range(N):
    xmaxlife=1
    while xmaxlife !=0 :
        dx=np.random.normal()
        xn = x[-1]+ dx
        print (xn)
        xn=absorbing(xn, murdroite, murgauche)
        x.append(xn)
print (x)


#vision horizontale
plt.subplot(211)
for i in range(N):
    plt.plot(x[i],3,'ob')
plt.title("déplacement du bonhomme")


#vision en fonction des pas
plt.subplot(212)
plt.plot(x,"^y")
plt.title("distance parcourue a chaque pas")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273

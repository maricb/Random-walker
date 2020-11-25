import random
import math
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
from random import randrange
from matplotlib import pyplot
seed(1)

x=[0]
N = int(input("number of steps : "))
nbonhomme = int(input("nombre de personne que vous voulez faire marcher : "))
murdroite = 5
murgauche = -5
xmaxlife = 1
l = 0
stock =np.zeros((nbonhomme,N+1))
nbonhommeenvie = nbonhomme


def reflect(xn,murdroite,murgauche):
    if xn > murdroite :
        xn=murdroite - abs(murdroite - xn)
    if xn < murgauche :
        xn = murgauche + abs(murgauche - xn)
    return(xn)


def absorbing(xn, murdroite, murgauche,xmaxlife):
    if xn>murdroite :
        xn=murdroite
        xmaxlife = 0
        l=1
        nbonhommeenvie -= 1

    if xn<murgauche :
        xn=murgauche
        xmaxlife = 0


    return(xn,xmaxlife, nbonhommeenvie)


def reflectabsord(N,xn,xmaxlife, nbonhommeenvie):
    p=np.random.random()
    if 0.5 < p :
        xn=reflect(xn, murdroite, murgauche)
    if 0.5 > p :
        xn,xmaxlife = absorbing(xn, murdroite, murgauche,xmaxlife)
    return(xn,xmaxlife,nbonhommeenvie)


for i in range(nbonhomme) :
    x = [0]
    xmaxlife=1
    p=np.random.choice([1,2,3])
    wn = [0]

    for z in range(N):

        dx=np.random.normal()
        xn = x[-1]+ dx

        if p==1 :

            if xmaxlife!=0:
                xn,xmaxlife, nbonhommeenvie = reflectabsord(N,xn,xmaxlife, nbonhommeenvie)
                wn.append(1)
                #les pas en abscisses en ordonnée le nombre de survivant
                wn.append(nbonhommeenvie)
            else:
                xn,xmaxlife=absorbing(xn, murdroite, murgauche,xmaxlife)
        x.append(xn)

    stock[i,:] = x
    print(wn)




plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273


#plot of the number of surviving walkers in the partially absorbing case as a function of N (number of steps)

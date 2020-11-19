# Créé par aaugr, le 17/11/2020 en Python 3.7

import random
import math
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
from random import randrange
from matplotlib import pyplot
seed(1)
#<<<<<<< HEAD

#creation de la liste qui contient les positions du deplacement
x=[0]
#nombre de pas fait par la personne alcoolisee
N = int(input("number of steps : "))
murdroite = 5
murgauche = -5
xmaxlife = 1
p=(len(x)//2*N)
#np.random.normal prend une valeur dans une fonction normale centree (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas

def reflect(xn,murdroite,murgauche):
    if xn > murdroite :
        xn=murdroite - abs(murdroite - xn)
    if xn < murgauche :
        xn = murgauche + abs(murgauche - xn)
    return(xn)


def absorbing(xn, murdroite, murgauche):
    xmaxlife=1
    i=0
    while xmaxlife != 0 :
        if xn>murdroite :
            xn=murdroite
            xmaxlife == 0
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


for i in range(N):
            dx=np.random.normal()
            xn = x[-1]+ dx
            p=np.random.random()
            if 0.5 < p :
                xn=reflect(xn, murdroite, murgauche)
            print (xn)
            if 0.5 > p :
                xn = absorbing(xn, murdroite, murgauche)

            x.append(xn)
            print(xmaxlife)
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
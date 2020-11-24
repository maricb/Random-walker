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
p=(len(x)/2*N)
ensemblebonhomme = {}
#np.random.normal prend une valeur dans une fonction normale centree (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas





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
        print("xmaxlife = 0")
    if xn<murgauche :
        xn=murgauche
        xmaxlife = 0
        print("xmaxlife = 0")
    return(xn,xmaxlife)

        #for i in range(N):

        #    while xmaxlife !=0 :
        #        dx=np.random.normal()
        #        xn = x[-1]+ dx
        #        print (xn)
        #        xn=absorbing(xn, murdroite, murgauche)
        #        x.append(xn)

plt.subplot(211)

for i in range(11) :
    x = [0]
    xmaxlife=1
    for z in range(N):
        dx=np.random.normal()
        xn = x[-1]+ dx
        p=np.random.random()
        if 0.5 < p :
            xn=reflect(xn, murdroite, murgauche)
        print (xn)
        if 0.5 > p :
            xn,xmaxlife = absorbing(xn, murdroite, murgauche,xmaxlife)
        if xmaxlife!=0:
            x.append(xn)

    ensemblebonhomme[i] = x
#dictionnaire


somme = 0
for numerobonhomme in range(11) :
    x = ensemblebonhomme.get(numerobonhomme)
    somme +=len(x)
#get = récup valeur associée à la clé 1
    for pas in range(len(x)):
        if numerobonhomme%2==0:
            plt.plot(x[pas],numerobonhomme,'ob')
        else:
            plt.plot(x[pas],numerobonhomme,'or')
        plt.title("déplacement du bonhomme")
average = somme/11
print (average)


#vision en fonction des pas
plt.subplot(212)
plt.plot(x,"^y")
plt.title("distance parcourue a chaque pas")
plt.xlabel("nombre de pas effectué")
plt.ylabel("coordonnée du pas")
plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273
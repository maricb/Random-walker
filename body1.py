# Créé par aaugr, le 17/11/2020 en Python 3.7

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
steps_reflecting = 0
#np.random.normal prend une valeur dans une fonction normale centree (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas

def reflect(xn,murdroite,murgauche, steps_reflecting):
    if xn > murdroite :
        steps_reflecting = murdroite - xn
        xn=murdroite - steps_reflecting

    if xn < murgauche :
        steps_reflecting = murgauche + xn
        xn = distanceN - steps_reflecting
    return(xn)


for i in range(N):
    dx=np.random.normal()
    xn = x[-1]+dx
    xn=reflect(xn,murdroite,murgauche, steps_reflecting)
    x.append(xn)
    #les murs
    if xn <-5 :
        xn+=1
    if xn >5:
        xn-=1









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

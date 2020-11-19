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
random_walk = list()
random_walk.append(-1 if random() <0.5 else 1)
for i in range(1, 1000) :
    movement = -1 if random() <0.5 else 1
    value = random_walk[i-1] + movement
    random_walk.append(value)
print (random_walk)
pyplot.plot(random_walk)
pyplot.show()
#=======
series =[randrange(10) for i in range(100)]
pyplot.plot(series)
pyplot.show()

#creation de la liste qui contient les positions du deplacement
x=[0]
#nombre de pas fait par la personne alcoolisee
N = int(input("number of steps : "))
distanceP = 5
distanceN = -5
steps_reflecting = [ ]
#np.random.normal prend une valeur dans une fonction normale centree (je crois hein pas sure du tout les cours de terminale remonte a looooooiiiiin)
#du coup elle permet de choisir une valeur probable pour la prochaine abscisse du pas

def reflect(xn,distanceP,distanceN, steps_reflecting):
    if xn > distanceP :
        steps_reflecting = distanceP - xn
        xn=distanceP - steps_reflecting

    if xn < distanceN :
        steps_reflecting = distanceN + xn
        xn = distanceN - steps_reflecting
    return(xn)


for i in range(N):
    dx=np.random.normal()
    xn = x[-1]+dx
    xn=reflect(xn,distanceP,distanceN, steps_reflecting)
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

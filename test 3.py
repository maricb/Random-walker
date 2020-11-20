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
    print (x)
        
plt.subplot(211)

for i in range(11) :
    x = [0]
    for z in range(N):
        dx=np.random.normal()
        xn = x[-1]+ dx
        p=np.random.random() 
        if 0.5 < p :
            xn=reflect(xn, murdroite, murgauche)
        print (xn)
        if 0.5 > p :
            xn,xmaxlife = absorbing(xn, murdroite, murgauche,xmaxlife)
        x.append(xn)
        print(xmaxlife)
        #if xmaxlife==0:
            #break      
    ensemblebonhomme[i] = x
           
   
   

    #vision horizontale
    #for j in range(11) : 
        #for t in range(len(x)):
            #for n in range(11):
                #plt.plot(x[t],j,'ob')
    #plt.plot(x[t]+1,j,'ob')
                
    #plt.title("déplacement du bonhomme")

    
for numérobonhomme in range(11) :
    x = ensemblebonhomme.get(numérobonhomme)
    for pas in range(len(x)):
        plt.plot(x[pas],numérobonhomme,'ob')
        plt.title("déplacement du bonhomme")



#vision en fonction des pas
plt.subplot(212)
plt.plot(x,"^y")
plt.title("distance parcourue a chaque pas")
plt.xlabel("nombre de pas effectué")
plt.ylabel("coordonnée du pas")
plt.show()
#>>>>>>> 52cfbbd8a21549b075332ba65b11eeb6d036c273
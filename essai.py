
import math
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
from random import randrange
from matplotlib import pyplot

x=[0]
N=50

for i in range(N):
    xn = x[-1]+np.random.normal()
    x.append(xn)
    if xn <-5 :
        xn+=1
    if xn >5:
        xn-=1


plt.subplot(211)
for i in range(N):
    plt.plot(x[i],3,'o-b')
plt.title("déplacement du bonhomme")

plt.subplot(212)
plt.plot(x,"^y")
plt.title("distance parcourue a chaque pas")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
plt.plot(x)
plt.show()


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
    x.append(x[-1]+np.random.normal())
plt.plot(x)
plt.show()
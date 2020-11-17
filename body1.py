# Créé par aaugr, le 17/11/2020 en Python 3.7

import math
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import randrange
from matplotlib import pyplot
seed(1)
series =[randrange(10) for i in range(100)]
pyplot.plot(series)
pyplot.show()
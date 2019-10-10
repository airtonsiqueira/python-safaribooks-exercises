import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [0, 2, 4, 6, 8, 10, 15, 20, 30, 40, 50, 100]
y = [random.randint(0, 50) for i in x]

plt.plot(x, y)
plt.ylabel("Valores")
plt.xlabel("Tempo em anos")
plt.show()

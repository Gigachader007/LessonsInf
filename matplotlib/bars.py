import matplotlib.pyplot as plt
import numpy as np
import random

names = [str(i) for i in range(7)]
data = [random.randint(0,100) for i in range(7)]

plt.bar(names,data)
plt.title("Числа")
plt.show()
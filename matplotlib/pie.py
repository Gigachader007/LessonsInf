import matplotlib.pyplot as plt
import numpy as np
import random

def Pie(n):
    labels = [str(i) for i in range(n)]
    values = [random.randint(0,2**n) for i in range(n)]
    plt.pie(values,labels=labels)
    plt.show()

Pie(int(input()))
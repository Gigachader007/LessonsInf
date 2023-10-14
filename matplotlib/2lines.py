import matplotlib.pyplot as plt
import numpy as np


#2 линии

def res(k1,k2,b1,b2):
    plt.title(f"Графики y1={k1}x{b1:+} и y2={k2}x{b2:+}")
    x = np.linspace(-1000,1000,100000)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x,k1*x+b1,"g--",x,k2*x+b2,"r--")
    plt.show()

res(*map(float,input().split()))
import matplotlib.pyplot as plt
import numpy as np

phi, L, g, X = map(float,input().split())
T = 2*np.pi*np.sqrt(L/g)
w = 2*np.pi / T
time = np.linspace(0,10,1000)
x = X*np.sin(w*time+phi)
y = (w**2) * (X**2) * (np.sin(w*time+phi)**2) / (2*g)

ax = plt.figure().add_subplot(projection = "3d")
ax.plot(time,x,y)

plt.show()
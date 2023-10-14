import matplotlib.pyplot as plt
import numpy as np

#4 графика

x = np.linspace(-10,10,100)

plt.subplot(2,2,1)
plt.title("y=cosx")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,np.cos(x))

plt.subplot(2,2,2)
plt.title("y=sinx")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,np.sin(x))

plt.subplot(2,2,3)
plt.title("y=x^2")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,x**2)

plt.subplot(2,2,4)
plt.title("y=2/4")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,2/x)

plt.show()
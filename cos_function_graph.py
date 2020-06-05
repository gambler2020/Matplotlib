import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,3*np.pi,num=100)
y=np.cos(x)
plt.title("Cos function graph", color="Green")
plt.xlabel("domain of cos function", color="red")
plt.ylabel("Range of cos function", color="red")
plt.plot(x,y)
plt.show()

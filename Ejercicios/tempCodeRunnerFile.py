import numpy as np
import matplotlib.pyplot as plt


array=np.array([[1,2,3,4],[1,2,3,4]]) # tiene que ser homogeneas

x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()

x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()
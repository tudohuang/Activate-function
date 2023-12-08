import numpy as np
import matplotlib.pyplot as plt
def LeakyReLU(x):
    return np.maximum(0.1*x,x)
def ReLU(x):
    return np.maximum(0,x)

plt.plot(x,LeakyReLU(x),label= 'LeakyReLU(x)')
plt.plot(x,ReLU(x),label= 'ReLU(x)')
plt.legend()
plt.show()

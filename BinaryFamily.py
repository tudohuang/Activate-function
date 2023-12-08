import matplotlib.pyplot as  plt
import numpy as np
def σ(x):
    return 1/(np.exp(-x)+1)
def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
def arctan(x):
    return np.arctan(x)
def step(x):
  return 1 if x > 0 else x =0
x_values = np.linspace(-1, 1, 100)
plt.plot(x, σ(x), label='σ(x)')
plt.plot(x, tanh(x), label='tanh(x)')
plt.plot(x,arctan(x),label = 'ArcTan(x)')
plt.plot(x_values,step(x_values),label = 'Step(x)')
plt.legend()
plt.grid(True)
plt.show()

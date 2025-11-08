import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(0, 1, 10000)   # σ = 1
x2 = np.random.normal(0, 3, 10000)   # σ = 3
x3 = np.random.normal(0, 0.5, 10000) # σ = 0.5

plt.hist(x1, bins=50, alpha=0.6, label='σ=1')
plt.hist(x2, bins=50, alpha=0.6, label='σ=3')
plt.hist(x3, bins=50, alpha=0.6, label='σ=0.5')
plt.legend()
plt.title("Effect of Standard Deviation on Normal Distribution")
plt.show()
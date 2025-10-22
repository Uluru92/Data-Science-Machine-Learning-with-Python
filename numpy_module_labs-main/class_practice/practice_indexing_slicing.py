import numpy as np

a = np.arange(10)
b =a
print(a)

b[0] = 9
print(a)
print(b)

a[:5] = np.arange(10,15)
print(a)
print(b)

a[:5] += 100
print(a)
print(b)
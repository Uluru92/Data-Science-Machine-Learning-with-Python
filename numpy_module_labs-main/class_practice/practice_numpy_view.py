import numpy as np

a = np.arange(12)
print(a[5:8])
b=a[5:8]
print(b)

b[0]=50
print(b)
print(a)

print(b.base) 
print(a.base) 
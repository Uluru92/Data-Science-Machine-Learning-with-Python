import numpy as np

# matrix multiplication
a = np.arange(1,10).reshape((3, 3))
b = np.arange(10,19).reshape((3, 3))

print(f'a: \n{a}')
print(f'b: \n{b}')

# matrix multiplication
c = np.dot(a,b) 
print(f'c: \n{c}')

# matrix multiplication - same as above
d = a.dot(b) 
print(f'd: \n{d}')

# matrix multiplication - same as above
e = a @ b 
print(f'e: \n{e}')

# matrix multiplication - same as above
f = np.matmul(a,b) 
print(f'f: \n{f}')

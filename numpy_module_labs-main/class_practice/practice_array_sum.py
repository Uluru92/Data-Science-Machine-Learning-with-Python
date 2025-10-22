import numpy as np

a = np.arange(1,10).reshape((3,3))

print(a)
print()
# sum of all elements
print(f'sum: {np.sum(a)}') 

# mean of all elements
print(f'mean: {np.mean(a)}')

# standard deviation of all elements
print(f'standard deviation: {np.std(a)}' )

print()
# sum of each column
print(f'sum of axis Y: {np.sum(a, axis=0) }')
print(f'sum of axis X: {np.sum(a, axis=1) }')

# If you are struggling to see it, then I 
# suggest using a non-symmetric matrix, such as:
a = np.arange(1,13).reshape((2, 6))
print(f'\nExample of asymetric array: \n{a}')
print()
# mean of each column, will be 6 values
print(f'sum axis 0: {a.sum(axis=0)}') 
# mean of each row, will be 2 values
print(f'sum axis 1: {a.sum(axis=1)}') 

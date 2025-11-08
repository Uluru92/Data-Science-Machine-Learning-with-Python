import numpy as np

a = np.arange(1,13).reshape((2, 6))
print("array a:")
print(a)
print()

print((f'\nsquare a: \n{np.sqrt(a)}'))
print((f'\nlong base a: \n{np.log(a)}'))
print((f'\nexponential a: \n{np.exp(a)}'))
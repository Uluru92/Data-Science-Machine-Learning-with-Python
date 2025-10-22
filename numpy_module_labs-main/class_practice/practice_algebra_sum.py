import numpy as np  

# we use reshape to create a 3x3 matrix for us 
# we will learn more about this later
a = np.arange(1,10).reshape((3, 3))  
b = np.arange(10,19).reshape((3, 3))
print(f"a: \n{a}")
print()
print(f"b: \n{b}")
print()


print(f"SUM a+b: \n{a + b}")
print(f"\nMultiplication a*b: \n{a * b}")
print(f"\nDivision b/a: \n{(b / a) }")
print(f"\nSubstraction b-a: \n{b - a}")
print(f"\nScalar multiplication a*3: \n{a*3}")
print(f"\nScalar division a/10: \n{a/10}")
print(f"\nScalar substraction a-5: \n{a-5}")
print(f"\nScalar square a**2: \n{a**2}")
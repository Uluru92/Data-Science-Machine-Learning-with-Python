# This is how you import NumPy. Everyone does it this way, so you should, too.
import numpy as np

# Create a 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

print(a.dtype)
print()
for element in a:
    print(element)
    print(type(element))
    print(element.dtype)
    print()

    # already did this
a = np.array([1, 2, 3, 4, 5]) 

# now using floats
b = np.array([1.0, 2.0, 3.0, 4.0, 5.0]) 
print(b.dtype)

# 2D array
multi_list_a = np.array([[1, 2, 3], [4, 5, 6]]) 
print(multi_list_a)
print()

# 2D array but with floats and using tuples
multi_list_b = np.array([(1.5, 2.1, 3), (4, 5, 6)]) 
print(multi_list_b)
import numpy as np

# Create a large array of a million elements
data = np.random.rand(1000000)

# Define a function for adding using a loop
def add_python_loop(arr):
    result = np.empty(len(arr))
    for i in range(len(arr)):
        # adding 1 to each element
        result[i] = arr[i] + 1  
    return result



add_python_loop(data) 
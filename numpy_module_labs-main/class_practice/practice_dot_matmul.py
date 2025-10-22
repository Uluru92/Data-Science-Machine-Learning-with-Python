import numpy as np
# Random 3D array of shape (2, 3, 4)
A = np.random.rand(2, 3, 4)  
# Random 3D array of shape (2, 4, 3)
B = np.random.rand(2, 4, 3)  

# Using np.dot
C_dot = np.dot(A, B)
print(C_dot.shape)  
# Outputs: (2, 3, 2, 3)

# Using @
C_matmul = A @ B
print(C_matmul.shape)  
# Outputs: (2, 3, 3)
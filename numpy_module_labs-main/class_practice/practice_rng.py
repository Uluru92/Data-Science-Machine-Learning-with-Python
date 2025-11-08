# Random Number Generator practice with seed
import numpy as np
rng = np.random.default_rng(42) # Create a random number generator with a seed
print(rng.uniform())
print(rng.uniform(low=0,high=5, size = (2,2)))
print(rng.integers(low=0,high=5, size = (2,2)))

list = ['dog', 'cat', 'horse', 'cat']
print(rng.choice(list, size=1, p=[0.15,0.15,0.7,0.0]))

print(rng.random(size=5)) 
print(rng.normal(loc=5.0, scale=1.0, size=5))
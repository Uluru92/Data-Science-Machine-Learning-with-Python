import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

housing = fetch_california_housing(as_frame=True)
X = housing.data
y = housing.target
X['MedInc'].hist(bins=80)

X.hist()
plt.show()
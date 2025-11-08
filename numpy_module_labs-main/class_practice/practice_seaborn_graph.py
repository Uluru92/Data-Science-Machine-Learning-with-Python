import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns


housing = fetch_california_housing(as_frame=True)
X = housing.data
y = housing.target


sns.set() # this sets the default seaborn style for all plots
sns.displot(X['MedInc'], bins=30, kde=True, aspect=2)

plt.show()



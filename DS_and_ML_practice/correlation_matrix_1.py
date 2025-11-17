import pandas as pd
from sklearn.datasets import fetch_california_housing
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

housing = fetch_california_housing(as_frame=True)
X = housing.data
corrs = X.corr()
fig, ax = plt.subplots()
mask = np.triu(np.ones_like(corrs, dtype=bool))
sns.heatmap(corrs, ax=ax, annot=True, cmap='YlGnBu', linewidths=0.2, fmt='.2f', mask=mask)
ax.set_title('Correlation matrix for California Housing dataset')

plt.show()
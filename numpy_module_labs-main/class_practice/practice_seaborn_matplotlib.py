import numpy as np
from scipy.spatial.distance import mahalanobis

# Generate a random multivariate dataset
n_samples = 1000
n_features = 3
mean = np.zeros(n_features)
cov = np.eye(n_features)
data = np.random.multivariate_normal(mean, cov, size=n_samples)

# Calculate the Mahalanobis distance for each point
mu = np.mean(data, axis=0)
Sigma = np.cov(data, rowvar=False)
dist = []
for i in range(n_samples):
    x = data[i]
    dist.append(mahalanobis(x, mu, Sigma))

# Calculate the threshold for identifying outliers
alpha = 0.01  # significance level
threshold = np.quantile(dist, 1 - alpha)

# Identify the outliers
outliers = np.where(dist > threshold)[0]

# Print the results
print("Number of outliers:", len(outliers))
print("Outlier indices:", outliers)

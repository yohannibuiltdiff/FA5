import itertools
import numpy as np
import matplotlib.pyplot as plt

population = [9, 12, 15]
probabilities = [1/3, 1/3, 1/3]

samples = list(itertools.product(population, repeat=2))

means = []  


for sample in samples:
    sample_mean = np.mean(sample)
    means.append(sample_mean)

mean = np.mean(means)

variance = np.var(means, ddof=1)

plt.hist(means, bins=20, density=True, alpha=0.6, color='b', edgecolor='k', label='Sampling Distribution')
plt.xlabel('Sample Mean')
plt.ylabel('Probability Density')
plt.title('Sampling Distribution of the Mean')
plt.axvline(x=np.mean(population), color='r', linestyle='--', label='Population Mean (μ)')
plt.legend()


plt.show()


print(f"Mean of Sample Means (μ_x̄): {mean}")
print(f"Variance of Sample Means (σ_x̄²): {variance}")

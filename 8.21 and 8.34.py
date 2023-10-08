###8.21

import itertools
import numpy as np


population = [3, 7, 11, 15]


sample_size = 2


population_mean = np.mean(population)


population_std = np.std(population)


samples = list(itertools.product(population, repeat=sample_size))


sample_means = [np.mean(sample) for sample in samples]


sampling_dist_mean = np.mean(sample_means)


sampling_dist_std = np.std(sample_means)

# Print the results
print(f"(a) Population Mean: {population_mean}")
print(f"(b) Population Standard Deviation: {population_std}")
print(f"(c) Mean of the Sampling Distribution of Means: {sampling_dist_mean}")
print(f"(d) Standard Deviation of the Sampling Distribution of Means: {sampling_dist_std}")
print(f"You can verify part (c) by noticing that the mean of the sampling distribution of means is the same as the population mean.") 
print(f"You can verify part (d) using the formula by dividing the population standard deviation by the square root of the sample size.")

###8.34
from math import comb

t = 200
prob = 0.5

less_40 = sum(comb(t, k) * (prob ** k) * ((1 - prob) ** (t - k)) for k in range(0, 80))
print("Probability that less than 40% will be boys :", less_40)

between_43_57 = sum(comb(t, k) * (prob ** k) * ((1 - prob) ** (t - k)) for k in range(86, 115))
print("Probability that between 43% and 57% will be girls :", between_43_57)

more_54 = sum(comb(t, k) * (prob ** k) * ((1 - prob) ** (t - k)) for k in range(110, 201))
print("Probability that more than 54% will be boys :", more_54)



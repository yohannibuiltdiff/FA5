import itertools

credits = [6, 9, 12, 15, 18]
probability = [0.1, 0.2, 0.4, 0.2, 0.1]

samples = list(itertools.product(credits, repeat=2))

means = []  
probabilities = []  


for sample in samples:
    sample_mean = sum(sample) / 2  
    means.append(sample_mean)
    
 
    sample_probability = 1.0
    for x in sample:
        sample_probability *= probability[credits.index(x)]
        probabilities.append(sample_probability)


for i in range(len(samples)):
    print(f"Sample {i + 1}: {samples[i]}, Mean: {means[i]}, Probability: {probabilities[i]}")

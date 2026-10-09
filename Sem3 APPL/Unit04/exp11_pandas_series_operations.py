import numpy as np
import pandas as pd

# Series of 10 random numbers
arr = pd.Series(np.random.randint(0,51, size=10))
print("Series:", arr)

# Indexing
print("First element:", arr[0])

# Filtering
print("Numbers greater than 25:", arr[arr > 25])

# Statistical operations
print("Mean:", arr.mean())
print("Median:", arr.median())
print("Minimum:", arr.min())
print("Maximum:", arr.max())
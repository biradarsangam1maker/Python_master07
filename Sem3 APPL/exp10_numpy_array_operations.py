import numpy as np

# 1D array
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("1D array: ", arr)

# Slicing
print("1D array slicing: ", arr[1:9:2])
print("First 5 elements: ", arr[0:5:1])
print("Every 2nd element: ", arr[0:10:2])

# Statistical measures
print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Maximum: ", np.max(arr))
print("Minimum: ", np.min(arr))

# Broadcasting
arr = arr + 5
print("Array after broadcasting: ", arr)
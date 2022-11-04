"""Alta3 Research | treich@alta3.com
  Numpy arrays and operations"""

import numpy as np

# Use the randint function to generate 1-, 2-, and 3-dimensional arrays
arr1d = np.random.randint(11, size=5) # 1-D array of 5 random integers between 0-10
arr2d = np.random.randint(11, size=(2, 3)) # 2-D array  spanning 2 rows, 3 cols
arr3d = np.random.randint(11, size=(2, 3, 4)) # 3-D array containing two 2-D arrays of 3 rows, 4 cols each 

print("One-dimensional array:", arr1d, sep="\n")
print("Two-dimensional array:", arr2d, sep="\n")
print("Three-dimensional array:", arr3d, sep="\n")


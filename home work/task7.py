import numpy as np
my_array = np.arange(12).reshape(3, 4)
print("Before swap:")
print(my_array)
my_array[:,[0, 1,2,3]] = my_array[:,[3,2,1, 0]]
print("\nAfter swap:")
print(my_array)
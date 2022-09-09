import numpy as np

original_array=[10, 20, 30]

np_array=np.array(original_array)

np_array=np.append(np_array,np.arange(40,91,10))
print(np_array)
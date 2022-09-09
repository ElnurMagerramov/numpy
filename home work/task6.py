import numpy as np

myArray=np.arange(15).reshape(3,5)
print(myArray,"\n\n")

myArray=np.asfarray(myArray/10)
print(myArray)
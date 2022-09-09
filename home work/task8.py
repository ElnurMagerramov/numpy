import numpy as np

myArray=["ani", "sam", "joe","azad", "samir", "JoSeph","Amin", "Samit", "Jounel"]
print(myArray)
myArray=np.array(myArray,str)
print("\n",myArray)

print("\n",np.char.capitalize(myArray))

print("\n",np.char.lower(myArray))

print("\n",np.char.upper(myArray))

print("\n",np.char.swapcase(myArray))

print("\n",np.char.title(myArray))
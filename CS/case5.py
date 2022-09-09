import numpy as np
from tabulate import tabulate

table=np.zeros(100, int).reshape(10,10)

table[:,[0,9]]=table[[0,9],:]=99
table[[1,8],[1,8]]=1
table[[2,7],2:8]=1
table[2:8,[2,7]]=1
table[4:6,4:6]=1

   
print(table)
print(tabulate(table,tablefmt="fancy_grid"))
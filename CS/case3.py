import numpy as np
from tabulate import tabulate

table=np.linspace(0.01,1,100).reshape(10,10)
print(table)

print(tabulate(table,tablefmt="fancy_grid"))


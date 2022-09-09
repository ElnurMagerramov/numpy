import numpy as np
from tabulate import tabulate

table=["Behram", "Abbasov", 26, 85, "Yusif", "Abdullayev", 22, 92,"Maryam", "Mecidova", 19, 88, "Vagif", "Hesenzade", 24, 79]
print(table)

table=np.array(table).reshape(4,4)
print(table)

col_headers=np.array(["Name", "Surname", "Age", "Mark"])
print(tabulate(table,headers=col_headers, tablefmt="fancy_grid"))
import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_excel(
    "C:/Users/elnur/OneDrive/Masaüstü/QSS/Python/Week2/Day2/home work/cars.xlsx"
)
plt.scatter(
    cars.hwy,
    cars.cty,
    c="green",
    linewidths=2,
    marker="1",
    edgecolor="green",
    label="intersection point",
)
plt.xlabel("Highway")
plt.ylabel("City")
plt.title("Relationship between highway and city")
plt.legend()
plt.show()

 #According to figure we can see that correlation coefficient is greater than zero and indicates a positive relationship

import numpy as np


np.random.seed(seed=101)
print("visualizing our 7x4 array (Rows=days, cols=Cities)")
print("Lagos, New York, Tokyo, Sydney")
temperatures = np.random.randint(low=-5, high=35, size=(7,4))

print(temperatures)

first_3_days = temperatures[:3, :]
print("first 3 days of the week")
print(first_3_days)







import numpy as np
import matplotlib.pyplot as plt

Ec = 0.5
values = []
for Eo in range(1,100):
    Xmax = (np.log(Eo)/np.log(Ec))/np.log(2)
    values.append(Xmax)
plt.plot(values) # plotting by columns
plt.show()
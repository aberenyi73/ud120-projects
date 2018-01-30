import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
data2 = np.array([[11,12,13],[14,15,16],[17,18,19]])
dz = zip(data1,data2)

#print data1, "\n"
#print data2, "\n"
#print dz, "\n"

for r in data1:
    print r[0], " ", r[1]
    plt.plot(data1[0], data1[1], 'ro')
    plt.plot(data2[0], data2[1], 'b^')

plt.show()
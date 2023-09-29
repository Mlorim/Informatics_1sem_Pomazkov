import matplotlib.pyplot as plt
import numpy as np

num = 10
mass = [0] * 4
for i in range(len(mass)):
    mass[i] = np.random.normal(83, 1.7, num)
    num **= 2

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.hist(mass[i], 70)

plt.show()

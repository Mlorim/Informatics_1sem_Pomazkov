import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

btc = pd.read_csv('BTC_data.csv', delimiter=',')

labels = [(i[8:10] + i[4:8] + i[:4]) for i in btc['time']]

time = [(int(i[8:10]) + int(i[5:7]) * 30 + int(i[:4]) * 365) for i in btc['time']]
cost = [int(i) for i in btc['close']]

plt.plot(time, cost, label='Accurate values')
plt.xticks(time, labels, rotation='vertical')
plt.xlabel("Date")
plt.ylabel("Close BTC cost")

polynom = np.polyfit(time, cost, 5)
approx_val = [np.poly1d(polynom)(x) for x in time]
plt.plot(time, approx_val, label='Approximated values')

plt.legend()
plt.show()

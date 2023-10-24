
import matplotlib.pyplot as plt
import pandas as pd


def LeastSquareMethod(x, y):
    n = len(x)
    sum_xy = sum([x[i] * y[i] for i in range(0, n)])
    sum_x2 = sum([i ** 2 for i in x])
    a = (n * sum_xy - sum(x) * sum(y)) / (n * sum_x2 - (sum(x) ** 2))
    b = (sum(y) - a * sum(x)) / n
    return [a, b]

fig = plt.figure(figsize=(16, 9))
graf2 = fig.add_subplot()


X = [64,49,36,25,16]
Y = [3.1441, 2.7582, 2.2867, 2.2538, 2.0301]
print(X)

graf2.plot(X, Y, '.', label='Accurate values')
graf2.set_title('Graph', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
graf2.set_xlabel('X, cm')
graf2.set_ylabel('Y, cm')

coeff = LeastSquareMethod(X, Y)
graf2.plot(X, [(x * coeff[0] + coeff[1]) for x in X], label='Approximated values', color="r")
graf2.legend()

print("Approximating line coefficients: a = ", coeff[0], "b = ", coeff[1])

plt.show()
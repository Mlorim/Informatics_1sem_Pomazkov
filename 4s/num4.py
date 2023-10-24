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
graf1 = fig.add_subplot(121)
graf2 = fig.add_subplot(122)

iris = pd.read_csv('iris_data.csv', delimiter=',')
print(iris)
length = len(iris["Id"])


sepal = []
for i in range(length):
    sepal.append([iris["SepalLengthCm"][i], iris["SepalWidthCm"][i]])

sepal.sort(key=lambda i: i[0])

petal = []
for i in range(length):
    petal.append([iris["PetalLengthCm"][i], iris["PetalWidthCm"][i]])

petal.sort(key=lambda i: i[0])


graf1.plot([i[0] for i in sepal], [i[1] for i in sepal], '.')
graf1.set_title('Sepal Combinations', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
graf1.set_xlabel('Length, cm')
graf1.set_ylabel('Width, cm')

petal_l = [i[0] for i in petal]
petal_w = [i[1] for i in petal]

graf2.plot(petal_l, petal_w, '.', label='Accurate values')
graf2.set_title('Petal Combinations', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
graf2.set_xlabel('Length, cm')
graf2.set_ylabel('Width, cm')

coeff = LeastSquareMethod(petal_l, petal_w)
graf2.plot(petal_l, [(x * coeff[0] + coeff[1]) for x in petal_l], label='Approximated values', color="r")
graf2.legend()

print("Approximating line coefficients: a = ", coeff[0], "b = ", coeff[1])

plt.show()

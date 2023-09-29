import numpy as np
import random as rd


def GenMass(n, a, b):
    mass_x = []
    mass_y = []
    mass_y_gauss = []
    mass_rez = []
    for i in range(n):
        mass_x.append(rd.randint(0, 1000))
        mass_y.append(a * mass_x[i] + b)

    mu = sum(mass_y) / len(mass_y)
    sigma = np.std(mass_y)

    for i in range(0, n, 2):
        rnd = rd.randint(0, 1000)
        mass_y_gauss.append(mass_y[i] + rnd)
        mass_y_gauss.append(mass_y[i+1] - rnd)

    # Проверка коэффинцентов сгенерированного набора:

    sum_xy = sum([mass_x[i] * mass_y_gauss[i] for i in range(0, n)])
    sum_x2 = sum([i ** 2 for i in mass_x])
    ar = (n * sum_xy - sum(mass_x) * sum(mass_y_gauss)) / (n * sum_x2 - (sum(mass_x) ** 2))
    br = (sum(mass_y_gauss) - a * sum(mass_x)) / n

    for i in range(n):
        mass_rez.append([mass_x[i], mass_y_gauss[i]])

    return(ar, br, mass_rez)

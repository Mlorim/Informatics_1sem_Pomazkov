def LeastSquareMethod(x, y):
    n = len(x)
    sum_xy = sum([x[i] * y[i] for i in range(0, n)])
    sum_x2 = sum([i ** 2 for i in x])
    a = (n * sum_xy - sum(x) * sum(y)) / (n * sum_x2 - (sum(x) ** 2))
    b = (sum(y) - a * sum(x)) / n
    return [a, b]

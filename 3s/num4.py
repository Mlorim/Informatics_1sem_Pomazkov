import numpy as np

n = int(input())
m = int(input())
a = np.zeros((n, m), dtype=np.int8)
b = []

x = 0
y = 0

a[x][y] = 1

for i in range(2, n * m + 1):
    if (y != m-1) and (a[x][y+1] == 0) and (a[x-1][y] != 0 or x == 0):
        a[x][y + 1] = i
        y += 1
    elif (x != n-1) and (a[x+1][y] == 0):
        a[x+1][y] = i
        x += 1
    elif (y != 0) and (a[x][y-1] == 0):
        a[x][y-1] = i
        y -= 1
    elif (a[x-1][y] == 0):
        a[x-1][y] = i
        x -= 1

print("Матрица до умножения:", a, sep="\n")
print(" ")

for i in range(n):
    b.append([i * a[i][j] for j in range(m)])

b = np.array(b).reshape((n, m))

print("Матрица после умножения:", b, sep="\n")

f = [int(i) for i in input().split()]
n = f[0]
f = f[1:]
for i in range(1, n+1):
    if f.count(i) == 0:
        print(i)
        break
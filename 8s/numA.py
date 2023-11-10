n = int(input())
points = []
for i in range(n):
    points.append([int(i) for i in input().split()])

X = [p[0] for p in points]
Y = [p[1] for p in points]

med = sum(X) / n

for i in range(len(X)):
    if X[i] == med:
        Y = Y[:i] + Y[i+1:]


ok = 1
ro_mass = [abs(x - med) for x in X]

for ro in ro_mass:
    ok *= (ro_mass.count(ro) % 2 == 0) + (ro == 0)

for y in Y:
    ok *= (Y.count(y) % 2 == 0)

if ok:
    print('Yes')
else:
    print('No')

def NOD(a, b):
    while (a != 0) and (b != 0):
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


f = [int(i) for i in input().split()]

a = f[0]
b = f[1]

d = NOD(a, b)

rez = []

print(d)

for x in range(max(a, b)):
    y1 = (d - a * x) / b
    y2 = (d + a * x) / b
    if (y2 * 10) % 10 == 0:
        rez.append([-x, int(y2)])
    if (y1 * 10) % 10 == 0:
        rez.append([x, int(y1)])

rez = rez[:4]

minpare = [100000, 1000000]
for i in rez:
    if ((abs(i[0]) + abs(i[1])) < (abs(minpare[0]) + abs(minpare[1]))) \
            or ((abs(i[0]) + abs(i[1])) == (abs(minpare[0]) + abs(minpare[1])) and i[0] < minpare[0]):
        minpare = i

print(*minpare, d)

f = [int(i) for i in input().split()]
a = f[0]
b = f[1]


def NOD(x, y):
    while (x != 0) and (y != 0):
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


NOK = (a * b / NOD(a, b))

if NOK == b or NOK == a:
    print(max(a, b) - min(a, b))
else:
    print(int(NOK - a - b))
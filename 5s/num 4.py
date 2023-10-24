f = [int(i) for  i in input().split()]
n = f[0]
m = f[1]


def separate(n, m, c, k):
    if n % 2 == 0 or m % 2 == 0:
        return c
    elif n == 1 or m == 1:
        return c + 4 ** k
    else:
        return separate(n // 2, n // 2, c + 4 ** k,  k + 1)


print(separate(n, m, 0, 0))

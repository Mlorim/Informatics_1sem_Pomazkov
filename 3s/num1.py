def Fibonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonachi(n-2) + Fibonachi(n-1)
print(Fibonachi(int(input())))

def PrimeFactors (n):
    factors = []
    if n == 1:
        factors.append(1)
    for i in range(1, int(n ** 1/2) + 1):
        if n % i == 0:
            if len(PrimeFactors (i)) == 2:
                factors.append(i)
    factors.append(n)
    return factors

# print((int(input())))
def fibstring(n, k, mass):
    if n == 1:
        return 'a'
    elif n == 2:
        return 'b'
    elif n == 3:
        return 'ab'[k-1]
    elif n == 4:
        return 'bab'[k-1]
    else:
        if mass[n-3] >= k:
            return fibstring(n-2, k, mass)
        else:
            return fibstring(n-1, k-mass[n-3], mass)


mass_all = []
t = int(input())
for i in range(t):
    mass = [int(i) for i in input().split()]
    mass_all.append([mass[0]+1, mass[1]])

max_n = sorted(mass_all, key=lambda i: i[0], reverse=True)[0][0]
fib_numbers = [1, 1]
for i in range(max_n-2):
    fib_numbers.append(fib_numbers[i] + fib_numbers[i+1])

for i in range(len(mass_all)):
    n = mass_all[i][0]
    k = mass_all[i][1]
    print(fibstring(n, k, fib_numbers))
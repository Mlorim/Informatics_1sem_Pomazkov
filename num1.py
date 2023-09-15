f = [int(i) for i in input().split()]
n = f[0]
f = f[1:]
for i in range(1, n+1):
    if f.count(i) == 0:
        print(i)
        break

# f = [int(i) for i in input().split()]
# n = f[0]
# f = f[1:]
# print(sum([i for i in range(n+1)]) - sum(f))

# f = [int(i) for i in input().split()]
# n = f[0]
# f = f[1:]
# print(sum([i for i in range(n+1)]) - sum([int(i) for i in input().split()]))
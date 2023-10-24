f = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

n = f[0]
k = f[1]

max_s = 0
for i in range(0, 2**n):
    s = A[i] + A[i ^ k]
    if s > max_s:
        max_s = s
print(max_s)
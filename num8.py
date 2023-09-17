n = int(input())
f = [int(i) for i in input().split(" ")]
for i in f:
    cont = 0
    for j in f:
        if i > j:
            cont += 1
    if cont == int(n / 2):
        print(i)
        break
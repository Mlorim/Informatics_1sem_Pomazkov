n = int(input())
f = [int(i) for i in input().split()]

money = 0
while len(f) > 1:
    max_id = []
    max_el = max(f)
    for i in range(len(f)):
        if f[i] == max_el:
            max_id.append(i)

    money += sum([max_el - el for el in f[0:max_id[-1]]])

    f = f[max_id[-1]+1:]
print(money)



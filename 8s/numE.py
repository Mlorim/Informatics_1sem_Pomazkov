n = int(input())
dct = dict()
for _ in range(n):
    mass = input().split()
    dct[mass[0]] = [int(i) for i in mass[1:]] + [mass[0]]

expressions = []
last = ''
while last != '0':
    last = input()
    if last != '0':
        expressions.append(last)

for exp in expressions:
    if len(exp) == 1:
        print('0')
    else:
        ok = 1
        for i in range(1, len(exp)):
            ok *= dct[exp[i]][0] == dct[exp[i-1]][1]
        if not(ok):
            print('error')
        else:
            matrices = []
            for i in exp:
                matrices.append(dct[i])

            order = ''
            while len(matrices) > 1:
                min_pr = 1000000
                min_ind = 0
                for mat in range(len(matrices) - 1):
                    if matrices[mat][0] * matrices[mat + 1][1] < min_pr:
                        min_pr = matrices[mat][0] * matrices[mat + 1][1]
                        min_ind = mat
                matrices[min_ind] = [matrices[min_ind][0], matrices[min_ind+1][1], matrices[min_ind][2]]
                order += matrices[min_ind][2] + matrices[min_ind+1][2]
                matrices[min_ind][2] = matrices[min_ind][2] + matrices[min_ind+1][2]
                matrices.pop(min_ind+1)
            rez = 0
            i = 0
            while len(order) != 2:
                new = str(i)
                txt = dct[order[0]][2] + dct[order[1]][2]
                dct[new] = [dct[order[0]][0], dct[order[1]][1], new]
                rez += dct[order[0]][0] * dct[order[0]][1] * dct[order[1]][1]
                order = order.replace(txt, new)
                order = order[1:]
                i += 1

            rez += dct[order[0]][0] * dct[order[0]][1] * dct[order[1]][1]
            print(rez)

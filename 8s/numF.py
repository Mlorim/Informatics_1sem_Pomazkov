ND = []
num_mass = []

while ND != [0, 0]:
    ND = [int(i) for i in input().split()]
    if ND != [0, 0]:
        ND.append(int(input()))
    num_mass.append(ND)
num_mass = num_mass[:-1]

for i in num_mass:

    order = dict()
    for s in '9876543210':
        s = int(s)
        order[s] = []

    n = i[0]
    d = i[1]
    num = str(i[2])
    for j in range(n):
        order[int(num[j])].append(j)

    index_to_delete = []
    for key in '0123456789':
        index_to_delete += order[int(key)]

    max1 = ''
    for ind in range(n):
        if ind not in index_to_delete[:d]:
            max1 += str(num[ind])

    max2 = ''
    max_el = max([i for i in order.keys() if order[i] != []])
    max_el_1 = max([i for i in order.keys() if order[i] != [] and i != max_el])
    l = len(str(max1))
    rest = l - len(order[max_el])
    ind_1 = 1
    ind_2 = 2
    max2_all = []

    for i in range(len(order[max_el]) - 1, -1, -1):
        if len(num) - order[max_el][i] >= (rest + 1):
            ind_1 = i - 1
            break

    for i in range(len(order[max_el_1])):
        if order[max_el][ind_1] < order[max_el_1][i]:
            ind_2 = i - 1
            break

    rest = l - ind_1
    max2 += str(max_el) * (ind_1 + 1)
    try:
        max2 += num[order[max_el_1][ind_2]:order[max_el_1][ind_2] - 1 + rest]
    except:
        max2 = 0

    max3 = ''
    max3 += str(max_el) * (len(order[max_el]) - 1)
    max3 += num[order[max_el][-1]:order[max_el][-1] - 1 + rest]

    max4 = max(int(max1), int(max2), int(max3))
    print(max4)

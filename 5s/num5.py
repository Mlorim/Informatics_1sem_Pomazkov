from itertools import combinations
f = [int(i) for i in input().split()]
n = f[0]
not_comp = f[1]
mass_not_comp = []
combs = []
for i in range(not_comp):
    mass_not_comp.append([int(i) for i in input().split()])

mass_not_comp_uniq = []
for i in mass_not_comp:
    i = sorted(i)
    if i not in mass_not_comp_uniq:
        mass_not_comp_uniq.append(i)
mass_not_comp_uniq.sort(key=lambda i: i[0])

txt = []
for i in range(1, n+1):
    txt.append(i)

for i in combinations(txt, 3):
    combs.append([int(i) for i in i])

rez = len(combs)

for i in combs:
    if i[:2] in mass_not_comp_uniq or [i[0], i[2]] in mass_not_comp_uniq or i[1:] in mass_not_comp_uniq:
        rez -= 1

print(rez)

street = [int(i) for i in input().split()]
street += [0, 0, 0]

i = 0
s = street[0]

while i < len(street) - 2:
    s += max(street[i+2], street[i+3])
    if street[i+2] > street[i+3]:
        i += 2
    else:
        i += 3

i1 = 1
s1 = street[1]

while i1 < len(street) - 2:
    s1 += max(street[i1+2], street[i1+3])
    if street[i1+2] > street[i1+3]:
        i1 += 2
    else:
        i1 += 3

print(max(s, s1))
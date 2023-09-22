txt = input()
dict = []
mirr_symbols = "AHIMOTUVWXY18EJSZ3L25"
for i in "AHIMOTUVWXY18":
    dict.append([i,i])
dict.append(["E", "3"])
dict.append(["J", "L"])
dict.append(["S", "2"])
dict.append(["Z", "5"])
dict.append(["3", "E"])
dict.append(["L", "J"])
dict.append(["2", "S"])
dict.append(["5", "Z"])

is_pol = 0
if txt == txt[::-1]:
    is_pol = 1

ok = 1
for i in txt:
    ok *= mirr_symbols.count(i)
if ok != 0:
    for i in range(int(len(txt)/2)):
        for mass in dict:
            if mass[0] == txt[i]:
                ok *= (mass[1] == txt[-i-1])

if ok != 0 and is_pol == 1:
    print(txt, "is a mirrored palindrom")
elif ok != 0:
    print(txt, "is a mirrored string")
elif is_pol == 1:
    print(txt, "is a regular palindrom")
else:
    print(txt, "is not a palindrom")
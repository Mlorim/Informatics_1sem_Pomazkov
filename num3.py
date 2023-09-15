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

is_mirr = 0
ok = 1
for i in txt:
    ok *= mirr_symbols.count(i)
# if ok != 0:
#     for  in txt
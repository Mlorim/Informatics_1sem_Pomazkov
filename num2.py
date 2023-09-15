txt = input()
g = int(txt[0])
n = (len(txt) - 2) // g
txt = txt[2:]
rez = ""
for i in range(g):
    for j in range(n):
        rez += txt[:n][::-1]
        txt = txt[n:]
print(rez)
txt = input().split()
for i in range(int(len(txt)/2) + 1):
    print(" ".join(txt[:2][::-1]), end = " ")
    txt = txt[2:]
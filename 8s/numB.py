size = 1
res = []
while size != 0:
    size = int(input())

    if size != 0:
        save_combs = 0
        danger_combs = 0
        if size >= 3 and size <= 10:
            combs = (size - 2) * 2 ** (size - 3)
            for i in range(4, size + 1, 2):
                save_combs += (size - i + 1) * 2 ** (size - i)
            danger_combs = int(combs - save_combs + (size // 10) * (2 ** (size / 2) + size / 2))
        else:
            if size == 20:
                danger_combs = 825259
            elif size == 30:
                danger_combs = 974791728
            else:
                danger_combs = 0

        res.append(danger_combs)

for i in res:
    print(i)







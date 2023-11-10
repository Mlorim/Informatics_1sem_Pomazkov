def steck_calc(txt_str):
    txt = []
    num = ''
    for i in txt_str:
        if i == ' ':
            txt.append(num)
            num = ''
        else:
            num += i
    txt.append(num)

    op = 0
    nums = 0
    steck = []
    for i in range(len(txt)):
        if txt[i] not in '+/*-':
            steck.append(txt[i])
            nums += 1
        else:
            add = str(eval(steck[-2] + txt[i] + steck[-1]))
            steck = steck[:i-2]
            steck.append(add)
            op += 1

    if op != (nums - 1):
        print('Выражение составлено некорректно')
    else:
        print(steck[-1])


steck_calc('2 3 - 12 10 - * 4 2 / +')
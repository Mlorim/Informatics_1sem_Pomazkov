def power(symb):
    if symb in '+-':
        return 1
    elif symb in '/*':
        return 2


def polish(txt_str):
    txt = []
    num = ''
    for i in txt_str:
        if i not in '+-/*':
            num += i
        else:
            txt.append(num)
            txt.append(i)
            num = ''
    txt.append(txt_str[-1])
    opers = []
    rez = ''
    for i in range(len(txt)):
        if txt[i] not in '-+/*':
            rez += ' ' + txt[i]
        else:
            if (opers == []) or (power(opers[-1]) < power(txt[i])):
                opers.append(txt[i])
            else:
                opers.append(txt[i])
                while len(opers) != 1 and power(opers[-2]) >= power(opers[-1]):
                    rez += ' ' + opers[-2]
                    opers = opers[:-2] + [opers[-1]]

        if i == len(txt) - 1:
            while len(opers) != 0:
                rez += ' ' + opers[-1]
                opers = opers[:-1]

    return rez[1:]


print(polish('10-7+7*6-4'))
print(polish('a+b*c-d'))
print(polish('5+8/3-8'))




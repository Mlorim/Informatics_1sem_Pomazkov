def power(symb):
    if symb in '+-':
        return 1
    elif symb in '/*':
        return 2


def rev_polish(txt_str):
    txt = []
    num = ''
    for i in txt_str:
        if i not in '()+-/*':
            num += i
        else:
            if num != '':
                txt.append(num)
            txt.append(i)
            num = ''
    txt.append(txt_str[-1])
    steck = []
    rez = ''

    for i in range(len(txt)):
        if txt[i] not in '()+-/*':
            rez += txt[i]
            rez += ' '
        elif txt[i] in '+-*/':
            steck.append(txt[i])
            while (len(steck) != 1) and (steck[-2] not in '()') \
                    and (power(steck[-2]) >= power(txt[i])):
                rez += steck[-2]
                rez += ' '
                steck = steck[:-2] + [steck[-1]]
        elif txt[i] == '(':
            steck.append(txt[i])
        elif txt[i] == ')':
            while len(steck) != 0 and steck[-1] != '(':
                rez += steck.pop()
                rez += ' '
            steck = steck[:-1]

        if i == (len(txt) - 1):
            while len(steck) != 0:
                if steck[-1] not in '()':
                    rez += steck.pop()
                    rez += ' '

    return rez


def polish(txt_str):
    txt_str = txt_str[:-1]
    txt = txt_str.split()
    steck = []

    for i in txt:
        if i in '+-*/':
            op2 = steck.pop()
            op1 = steck.pop()
            exp = i + ' ' + op1 + ' ' + op2
            steck.append(exp)
        else:
            steck.append(i)

    return steck.pop()


print(polish(rev_polish('(2-3)*(12-10)+4/2')))
print(polish(rev_polish('(3+4*(2-1))/5')))
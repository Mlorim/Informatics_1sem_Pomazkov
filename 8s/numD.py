txt = input()
if (txt.count('(') == txt.count(')')) and (txt.count('{') == txt.count('}')) and (txt.count('[') == txt.count(']')):
    while ('()' in txt) or ('[]' in txt) or ('{}' in txt):
        if ('()' in txt):
            txt = txt.replace('()', '')
        if ('[]' in txt):
            txt = txt.replace('[]', '')
        else:
            txt = txt.replace('{}', '')

if txt == '':
    print('Yes')
else:
    print('No')
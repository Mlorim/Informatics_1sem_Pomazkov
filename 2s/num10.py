txt = input() + " "
consonants = "бвгджзйклмнпрстфхцчшщ"
vowels = "аеёиоуыэюя"
rez = ""
for i in range(len(txt)):
    symb = txt[i].lower()
    rez += symb
    if symb in vowels:
        if i == 0:
           continue
        elif txt[i-1:i+1] in "ьяьёьеью":
            if txt[i-1:i+1] == "ья":
                rez += ("c" + "а")
            elif txt[i-1:i+1] == "ьё":
                rez += ("c" + "о")
            elif txt[i - 1:i + 1] == "ье":
                rez += ("c" + "э")
            elif txt[i - 1:i + 1] == "ью":
                rez += ("c" + "у")
        elif txt[i-1] in consonants or (txt[i-1] in "ьъ" and txt[i+1] not in vowels):
            rez += ("c" + symb)

print(rez)
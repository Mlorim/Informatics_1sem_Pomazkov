def Triangular(size, symb):
    if size % 2 == 1:
        for i in range(1, size // 2 + 2):
            print(symb * i)
        for i in range(1, size // 2 + 1):
            print(symb * (size // 2 + 1 - i))
    else:
        for i in range(1, size // 2 + 1):
            print(symb * i)
        for i in range(size // 2, 0, -1):
            print(symb * i)

def len_line(cord1, cord2):
    return (((cord1[0] - cord2[0]) ** 2) + ((cord1[1] - cord2[1]) ** 2)) ** 0.5


def ic(text):
    if str(text)[-2:] == '.0':
        return str(text) + '0'
    else:
        return text


def div_line(cord1, cord2, l1):
    ln = len_line(cord1, cord2)
    h = l1 / (ln - l1)
    x = (cord1[0] + h * cord2[0]) / (h + 1)
    y = (cord1[1] + h * cord2[1]) / (h + 1)
    return [x, y]


n = int(input())
for i in range(n):
    main = [int(j) for j in input().split()]
    k = main[0]
    t = main[1]
    points = []

    for point in range(k):
        points.append([float(j) for j in input().split()])

    length = 0
    for pnt in range(1, k):
        length += len_line(points[pnt], points[pnt-1])
    gap_const = length / (t - 1)
    gap = gap_const

    print('Road #' + str(n) + ':')
    print(*[ic(round(el, 2)) for el in points[0]])

    for pnt in range(1, t-1):
        if gap + gap_const >= len_line(points[pnt], points[pnt-1]):
            cords = div_line(points[pnt-1], points[pnt], gap)
            gap = gap_const + gap - len_line(points[pnt], points[pnt-1])
        else:
            cords = div_line(points[pnt - 1], points[pnt], gap)
            gap = gap_const
            points = points[:pnt+1] + [points[pnt+1]] + points[pnt+1:]
            points[pnt+1] = points[pnt]
            points[pnt] = cords
        print(*[round(el, 2) for el in cords])
    print(*[ic(round(el, 2)) for el in points[-1]])


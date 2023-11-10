from itertools import combinations


class Vector():

    def __init__(self, set_mass):
        ok = 1
        for i in set_mass:
            ok *= (isinstance(i, int) or isinstance(i, float))
        assert ok, 'В векторе могут лежать только числа'
        mass = [float(i) for i in set_mass]
        self.x = mass[0]
        self.y = mass[1]
        self.z = mass[2]

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector([self.x + other.x, self.y + other.y, self.z + other.z])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([self.x + other, self.y + other, self.z + other])

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector([self.x - other.x, self.y - other.y, self.z - other.z])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([self.x - other, self.y - other, self.z - other])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([self.x * other, self.y * other, self.z * other])

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return self - other

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


def square(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    return s


''' point = [x, y, x], где xyz - координаты точки'''

points = [[1, 2, 0], [1, 3, 0], [4, 2, 0]]
txt = ""
for i in range(len(points)):
    txt += str(i)

triples = []
for i in combinations(txt, 3):
    triples.append([int(j) for j in i])

max_square = 0
for triple in triples:
    r1 = Vector(points[triple[0]]) #радиус векторы точек
    r2 = Vector(points[triple[1]])
    r3 = Vector(points[triple[2]])

    v1 = r2 - r1
    v2 = r3 - r2
    v3 = r1 - r3
    s = square(abs(v1), abs(v2), abs(v3))
    if s > max_square:
        max_square = round(s, 3)

print(max_square)
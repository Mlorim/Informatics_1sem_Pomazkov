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

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


''' point = [x, y, x, m], где xyz - координаты точки, а m - ее масса'''

points = [[1, 3, 4, 6], [2, 4, 4, 10], [6, 3, 9, 6], [10, 2, 43, 65]]

l = len(points)
pnt_x = [point[0] for point in points]
pnt_y = [point[1] for point in points]
pnt_z = [point[2] for point in points]
pnt_m = [point[3] for point in points]
sum_m = sum(pnt_m)

CM_x = sum([pnt_x[i] * pnt_m[i] for i in range(l)]) / sum_m
CM_y = sum([pnt_y[i] * pnt_m[i] for i in range(l)]) / sum_m
CM_z = sum([pnt_z[i] * pnt_m[i] for i in range(l)]) / sum_m
vCM = Vector([CM_x, CM_y, CM_z])

print(str(vCM))
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
            return Vector({self.x + other.x, self.y + other.y, self.z + other.z})
        elif isinstance(other, int) or isinstance(other, float):
            return Vector({self.x + other, self.y + other, self.z + other})

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector({self.x - other.x, self.y - other.y, self.z - other.z})
        elif isinstance(other, int) or isinstance(other, float):
            return Vector({self.x - other, self.y - other, self.z - other})

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector({self.x * other, self.y * other, self.z * other})

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


v1 = Vector({1, 2, 3})
v2 = Vector({2, 3, 4})
v3 = v1 * v2
print(str(v3))

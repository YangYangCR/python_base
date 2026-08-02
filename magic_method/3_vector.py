class Vector:
    """二维向量，演示运算符重载"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # === 算术运算符 ===
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x // other, self.y // other)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x % other, self.y % other)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x ** other, self.y ** other)
        return NotImplemented

    # === 反向运算符 ===
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Vector(other - self.x, other - self.y)

    # === 一元运算符 ===
    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return self

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# === 测试 ===
print("\n" + "=" * 70)
print("3. 运算符重载测试")
print("=" * 70)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}\n")

print(f"v1 + v2 = {v1 + v2}")  # __add__
print(f"v1 - v2 = {v1 - v2}")  # __sub__
print(f"v1 * 3 = {v1 * 3}")  # __mul__
print(f"3 * v1 = {3 * v1}")  # __rmul__
print(f"v1 / 2 = {v1 / 2}")  # __truediv__
print(f"v1 // 2 = {v1 // 2}")  # __floordiv__
print(f"v1 % 2 = {v1 % 2}")  # __mod__
print(f"v1 ** 2 = {v1 ** 2}")  # __pow__
print(f"-v1 = {-v1}")  # __neg__
print(f"abs(v1) = {abs(v1):.2f}")  # __abs__
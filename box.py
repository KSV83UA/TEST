class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __volume(self):
        return self.x * self.y * self.z

    def __lt__(self, other):
        return self.__volume() < other.__volume()

    def __le__(self, other):
        return self.__volume() <= other.__volume()

    def __gt__(self, other):
        return self.__volume() > other.__volume()

    def __str__(self):
        return f'{self.x}x{self.y}x{self.z}'


x_1 = Box(2, 3, 4)
x_2 = Box(6, 2, 1)

print(x_1 < x_2)
print(x_1 > x_2)
print(x_1 == x_2)
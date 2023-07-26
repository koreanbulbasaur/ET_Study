import math


class Circle:
    def __init__(self, radius) -> None:
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = value


circle = Circle(10)
print("# 원의 둘레와 넓이를 구함")
print("원의 둘레 :", circle.get_circumference())
print("원의 넓이 :", circle.get_area())
print('-'*20)

print("# __radius에 접근함")
print(circle.get_radius())
print('-'*20)

circle.set_radius(2)
print("원의 둘레 :", circle.get_circumference())
print("원의 넓이 :", circle.get_area())

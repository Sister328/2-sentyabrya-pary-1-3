import math


class Figure:
    def __init__(self, coords):
        self.__x, self.__y = coords

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, coords):
        self.__x, self.__y = coords

    def calculate_area(self):
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")


class Circle(Figure):
    def __init__(self, coords, radius):
        super().__init__(coords)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Square(Figure):
    def __init__(self, coords, side):
        super().__init__(coords)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


figures = [
    Circle((0, 0), 5),
    Square((10, 10), 4),
    Circle((20, 20), 3),
    Square((30, 30), 6),
    Circle((40, 40), 2),
]

total_area = 0

for figure in figures:
    area = figure.calculate_area()
    print(f"{type(figure).__name__}: площадь = {area:.2f}")
    total_area += area

print(f"Общая площадь всех фигур: {total_area:.2f}")

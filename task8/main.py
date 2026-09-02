class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print("Рисуется линия...")


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print("Рисуется прямоугольник...")


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print("Рисуется эллипс...")


class Triangle(Figure):
    def __init__(self, coords, width, color, side):
        super().__init__(coords, width, color)
        self.side = side

    def draw(self):
        print("Рисуется треугольник...")


figures = [
    Line((0, 0), 2, "black", 100),
    Rect((10, 10), 3, "blue", 50),
    Ellipse((20, 20), 4, "green", 25),
    Triangle((30, 30), 2, "red", 40),
]

# Цикл такой же, как в задаче 7: менять его не нужно.
for figure in figures:
    figure.draw()

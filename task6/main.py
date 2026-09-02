class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius


line = Line((0, 0), 2, "black", 100)
rect = Rect((10, 10), 3, "blue", 50)
ellipse = Ellipse((20, 20), 4, "green", 25)

print("Line:", line.coords, line.width, line.color, line.length)
print("Rect:", rect.coords, rect.width, rect.color, rect.height)
print("Ellipse:", ellipse.coords, ellipse.width, ellipse.color, ellipse.radius)

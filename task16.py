import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []

for _ in range(217):
    cls = random.choice((Line, Rect, Ellipse))
    a, b, c, d = [random.randint(-100, 100) for _ in range(4)]
    elements.append(cls(a, b, c, d))

for element in elements:
    if isinstance(element, Line):
        element.sp = (0, 0)
        element.ep = (0, 0)

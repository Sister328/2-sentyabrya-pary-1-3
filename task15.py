class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = [Point(1 + 2 * i, 1 + 2 * i) for i in range(1000)]
points[1].color = "yellow"

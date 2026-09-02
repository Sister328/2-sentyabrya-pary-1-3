class Graph:
    def __init__(self, x=0, y=0, scale=1.0):
        self._x = x
        self._y = y
        self._scale = scale

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        self._scale *= factor

    def get_state(self):
        return f"x={self._x}, y={self._y}, scale={self._scale}"


graph1 = Graph()
graph2 = Graph(10, 10, 1.0)
graph3 = Graph(20, 20, 2.0)

graph1.move(5, 3)
graph2.change_scale(2)

print("График 1:", graph1.get_state())
print("График 2:", graph2.get_state())
print("График 3:", graph3.get_state())

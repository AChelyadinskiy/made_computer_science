from base_figure import BaseFigure


class Rectangle(BaseFigure):
    """Class providing basic functionality for rectangle figures"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

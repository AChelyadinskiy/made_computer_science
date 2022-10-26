from base_figure import BaseFigure
from math import pi


class Circle(BaseFigure):
    def __init__(self, r):
        self.r = r

    def square(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r

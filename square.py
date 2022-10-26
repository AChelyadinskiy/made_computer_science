from rectangle import Rectangle


class Square(Rectangle):
    """Class providing basic functionality for square figures"""

    def __init__(self, a):
        super().__init__(a, a)

from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Сторона данной фигуры не должна быть отрицательным или нулевым значением")
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = "Square"

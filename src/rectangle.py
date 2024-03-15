from figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Сторона данной фигуры не должна быть отрицательным или нулевым значением")
        self.side_a = side_a
        self.side_b = side_b
        self.name = "Rectangle"

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

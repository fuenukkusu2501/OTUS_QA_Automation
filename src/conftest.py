import pytest


@pytest.fixture()
def rectangle_data():

    def _wrapper(data: str):
        if data == "integer_area":
            return 3, 5, 15
        if data == "float_area":
            return 3.5, 5.5, 19.25
        if data == "integer_perimeter":
            return 3, 5, 16
        if data == "float_perimeter":
            return 3.5, 5.5, 18
        if data == "minus":
            return -3, 5
        if data == "zero":
            return 3.5, 0

    yield _wrapper

    print("\nDown")


@pytest.fixture()
def square_data():

    def _wrapper(data: str):
        if data == "integer_area":
            return 5, 25
        if data == "float_area":
            return 5.5, 30.25
        if data == "integer_perimeter":
            return 5, 20
        if data == "float_perimeter":
            return 5.5, 22
        if data == "minus":
            return -5
        if data == "zero":
            return 0

    yield _wrapper

    print("\nDown")


@pytest.fixture()
def triangle_data():

    def _wrapper(data: str):
        if data == "integer_area":
            return 2, 4, 5, 3.799671038392666 #периметр 11
        if data == "float_area":
            return 2.2, 4.5, 5.2, 4.925935824795123
        if data == "integer_perimeter":
            return 2, 4, 5, 11
        if data == "float_perimeter":
            return 2.2, 4.5, 5.2, 11.9
        if data == "minus":
            return 3.5, 5.5, -1
        if data == "zero":
            return 3.5, 5.5, 0
        if data == "a + b < c":
            return 2, 3, 6
        if data == "a + b = c":
            return 2, 4, 6

    yield _wrapper

    print("\nDown")


@pytest.fixture()
def circle_data():

    def _wrapper(data: str):
        if data == "integer_area":
            return 4, 50.26548245743669
        if data == "float_area":
            return 4.5, 63.61725123519331
        if data == "integer_perimeter":
            return 4, 25.132741228718345
        if data == "float_perimeter":
            return 4.5, 28.274333882308138
        if data == "minus":
            return -1
        if data == "zero":
            return 0

    yield _wrapper

    print("\nDown")

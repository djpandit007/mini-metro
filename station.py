from enum import Enum, unique


@unique
class ShapeEnum(Enum):
    CIRCLE = 1
    SQUARE = 2
    TRIANGLE = 3


class Station(object):
    def __init__(self, shape):
        try:
            self.shape = ShapeEnum[shape.upper()]
        except KeyError:
            print("Shape '" + shape + "' not found in ShapeEnum")

    def get_shape(self):
        return self.shape

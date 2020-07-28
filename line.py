from enum import Enum, unique


@unique
class ColorEnum(Enum):
    BLUE = 1
    GREEN = 2
    RED = 3


class Line(object):
    def __init__(self, color):
        try:
            self.color = ColorEnum[color.upper()]
        except KeyError:
            print("Color '" + color + "' not found in ColorEnum")

    def get_color(self):
        return self.color


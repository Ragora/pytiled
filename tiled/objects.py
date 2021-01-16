class Color:
    """
        Class representing a color.
    """

    red: int = None
    """
        The red component of the color.
    """

    green: int = None
    """
        The green component of the color.
    """

    blue: int = None
    """
        The blue component of the color.
    """

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self) -> str:
        """
            Generates a textual representation of this object.
        """
        return "<Color RGB %u, %u, %u>" % (self.red, self.green, self.blue)

    def __str__(self) -> str:
        """
            Primary export function of this class - it will generate an HTML hex color
            representation of this object.
        """
        result = hex(self.blue | self.green << 8 | self.red << 16)[2:].upper()
        if len(result) < 6:
            padding = 6 - len(result)
            result = "".join(["0"] * padding) + result
        return "#" + result

    @classmethod
    def from_hex(class_object, hex: str):
        hex = int(hex.lstrip("#"), 16)
        red = hex >> 16 & 0xFF
        green = hex >> 8 & 0xFF
        blue = hex & 0xFF
        return class_object(red=red, green=green, blue=blue)

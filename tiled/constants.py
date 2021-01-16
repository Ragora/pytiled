import enum

class Orientation(enum.Enum):
    orthogonal = "orthogonal"
    isometric = "isometric"
    staggered = "staggered"
    hexagonal = "hexagonal"

class RenderOrder(enum.Enum):
    right_down = "right-down"
    right_up = "right-up"
    left_down = "left-down"
    left_up = "left-up"

class StaggerAxis(enum.Enum):
    x = "x"
    y = "y"

class StaggerIndex(enum.Enum):
    odd = "odd"
    even = "even"

class Compression(enum.Enum):
    zlib = "zlib"
    gzip = "gzip"
    zstd = "zstd"
    none = ""

class DrawOrder(enum.Enum):
    topdown = "topdown"
    index = "index"

class Encoding(enum.Enum):
    csv = "csv"
    base64 = "base64"

class Type(enum.Enum):
    tilelayer = "tilelayer"
    objectgroup = "objectgroup"
    imagelayer = "imagelayer"
    group = "group"

class Alignment(enum.Enum):
    unspecified = "unspecified"
    topleft = "topleft"
    top = "top"
    topright = "topright"
    left = "left"
    center = "center"
    right = "right"
    bottomleft = "bottomleft"
    bottom = "bottom"
    bottomright = "bottomright"

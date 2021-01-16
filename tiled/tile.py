import marshmallow

from . import layer, frame

class Tile(marshmallow.Schema):
    animation = marshmallow.fields.List(marshmallow.fields.Nested(frame.Frame))
    """
        Array of :ref:`Frames <json-frame>`
    """

    id = marshmallow.fields.Int(required=True)
    """
        Local ID of the tile
    """

    image = marshmallow.fields.Str(required=False)
    """
        Image representing this tile (optional)
    """

    imageheight = marshmallow.fields.Int(required=True)
    """
        Height of the tile image in pixels
    """

    imagewidth = marshmallow.fields.Int(required=True)
    """
        Width of the tile image in pixels
    """

    objectgroup = marshmallow.fields.Nested(layer.Layer, required=False)
    """
        Layer with type objectgroup, when collision shapes are specified (optional)
    """

    probability = marshmallow.fields.Float(required=False)
    """
        Percentage chance this tile is chosen when competing with others in the editor (optional)
    """

    properties = marshmallow.fields.List(marshmallow.fields.Dict(), required=True)
    """
        Array of :ref:`Properties <json-property>`
    """

    terrain = marshmallow.fields.List(marshmallow.fields.Int(), required=False)
    """
        Index of terrain for each corner of tile (optional)
    """

    type = marshmallow.fields.Str(required=False)
    """
        The type of the tile (optional)
    """
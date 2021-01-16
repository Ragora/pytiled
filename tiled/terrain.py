import marshmallow

class Terrain(marshmallow.Schema):
    name = marshmallow.fields.Str(required=True)
    """
        Name of terrain
    """

    properties = marshmallow.fields.List(marshmallow.fields.Dict(), required=True)
    """
        Array of :ref:`Properties <json-property>`
    """

    tile = marshmallow.fields.Int(required=True)
    """
        Local ID of tile representing terrain
    """

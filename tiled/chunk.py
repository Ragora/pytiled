import marshmallow

class Chunk(marshmallow.Schema):
    """
        Chunks are used to store the tile layer data for :doc:`infinite maps </manual/using-infinite-maps>`.
    """

    data = marshmallow.fields.Field(required=True)
    """
        Array of unsigned int (GIDs) or base64-encoded data
    """

    height = marshmallow.fields.Int(required=True)
    """
        Height in tiles
    """

    width = marshmallow.fields.Int(required=True)
    """
        Width in tiles
    """

    x = marshmallow.fields.Int(required=True)
    """
        X coordinate in tiles
    """

    y = marshmallow.fields.Int(required=True)
    """
        Y coordinate in tiles
    """
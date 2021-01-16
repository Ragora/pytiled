import marshmallow

class Point(marshmallow.Schema):
    x = marshmallow.fields.Float(required=True)
    """
        X coordinate in pixels
    """

    y = marshmallow.fields.Float(required=True)
    """
        Y coordinate in pixels
    """
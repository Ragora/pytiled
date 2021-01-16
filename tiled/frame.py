import marshmallow

class Frame(marshmallow.Schema):
    duration = marshmallow.fields.Int(required=True)
    """
        Frame duration in milliseconds
    """

    tileid = marshmallow.fields.Int(required=True)
    """
        Local tile ID representing this frame
    """

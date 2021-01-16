import marshmallow

from . import point

class Object(marshmallow.Schema):
    ellipse = marshmallow.fields.Boolean(required=True)
    """
        Used to mark an object as an ellipse
    """

    gid = marshmallow.fields.Int(required=True)
    """
        Global tile ID, only if object represents a tile
    """

    height = marshmallow.fields.Float(required=True)
    """
        Height in pixels.
    """

    id = marshmallow.fields.Int(required=True)
    """
        Incremental ID, unique across all objects
    """

    name = marshmallow.fields.String(required=True)
    """
        String assigned to name field in editor
    """

    polygon = marshmallow.fields.List(marshmallow.fields.Nested(point.Point), required=True)
    """
        Array of :ref:`Points <json-point>`, in case the object is a polygon
    """

    polyline = marshmallow.fields.List(marshmallow.fields.Nested(point.Point), required=True)
    """
        Array of :ref:`Points <json-point>`, in case the object is a polyline
    """

    point = marshmallow.fields.Boolean(required=True)
    """
        Used to mark an object as a point
    """

    properties = marshmallow.fields.List(marshmallow.fields.Dict(), required=True)
    """
        Array of :ref:`Properties <json-property>`
    """

    rotation = marshmallow.fields.Float(required=True)
    """
        Angle in degrees clockwise
    """

    template = marshmallow.fields.Str(required=True)
    """
        Reference to a template file, in case object is a :doc:`template instance </manual/using-templates>`
    """

    text = marshmallow.fields.Str(required=True)
    """
        Only used for text objects
    """

    type = marshmallow.fields.Str(required=True)
    """
        String assigned to type field in editor  
    """

    visible = marshmallow.fields.Boolean(required=True)
    """
        Whether object is shown in editor.
    """

    width = marshmallow.fields.Float(required=True)
    """
        Width in pixels.
    """

    x = marshmallow.fields.Float(required=True)
    """
        X coordinate in pixels
    """

    y = marshmallow.fields.Float(required=True)
    """
        Y coordinate in pixels
    """
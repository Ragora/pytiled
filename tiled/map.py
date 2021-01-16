import marshmallow

from . import constants, tileset, layer, objects

class Map(marshmallow.Schema):
    backgroundcolor = marshmallow.fields.Str(required=False)
    """
        Hex-formatted color (#RRGGBB or #AARRGGBB) (optional)
    """

    compressionlevel = marshmallow.fields.Int(required=True)
    """
        The compression level to use for tile layer data (defaults to -1, which means to use the algorithm default)
    """

    height = marshmallow.fields.Int(required=True)
    """
        Number of tile rows
    """

    hexsidelength = marshmallow.fields.Int(required=False)
    """
        Length of the side of a hex tile in pixels (hexagonal maps only)
    """

    infinite = marshmallow.fields.Bool(required=True)
    """
        Whether the map has infinite dimensions
    """

    layers = marshmallow.fields.List(marshmallow.fields.Nested(layer.Layer, required=False, default=[]))
    """
        Array of :ref:`Layers <json-layer>`
    """

    nextlayerid = marshmallow.fields.Int(required=True)
    """
        Auto-increments for each layer
    """

    nextobjectid = marshmallow.fields.Int(required=True)
    """
        Auto-increments for each placed object
    """

    orientation = marshmallow.fields.Str(required=True, validate=marshmallow.validate.OneOf(choices=[
        constants.Orientation.orthogonal.value,
        constants.Orientation.isometric.value,
        constants.Orientation.staggered.value,
        constants.Orientation.hexagonal.value,
    ]))
    """
        orthogonal, isometric, staggered or hexagonal
    """

    properties = marshmallow.fields.List(marshmallow.fields.Dict(), required=False, default=[])
    """
        Array of :ref:`Properties <json-property>`
    """

    editorsettings = marshmallow.fields.Dict(required=True)

    renderorder = marshmallow.fields.Str(required=True, validate=marshmallow.validate.OneOf(choices=[
        constants.RenderOrder.right_down.value,
        constants.RenderOrder.right_up.value,
        constants.RenderOrder.left_down.value,
        constants.RenderOrder.left_up.value
    ]))
    """
        right-down (the default), right-up, left-down or left-up (currently only supported for orthogonal maps)
    """

    staggeraxis = marshmallow.fields.Str(required=False, validate=marshmallow.validate.OneOf(choices=[
        constants.StaggerAxis.x.value,
        constants.StaggerAxis.y.value
    ]))
    """
        x or y (staggered / hexagonal maps only)
    """

    staggerindex = marshmallow.fields.Str(required=False, validate=marshmallow.validate.OneOf(choices=[
        constants.StaggerIndex.odd.value,
        constants.StaggerIndex.even.value
    ]))
    """
        odd or even (staggered / hexagonal maps only)
    """

    tiledversion = marshmallow.fields.Str(required=True)
    """
        The Tiled version used to save the file
    """

    tileheight = marshmallow.fields.Int(required=True)
    """
        Map grid height
    """

    tilesets = marshmallow.fields.List(marshmallow.fields.Nested(tileset.TileSet), required=True)
    """
        Array of :ref:`Tilesets <json-tileset>`
    """

    tilewidth = marshmallow.fields.Int(required=True)
    """
        Map grid width
    """

    type = marshmallow.fields.Str(required=True)
    """
        map (since 1.0)
    """

    version = marshmallow.fields.Float(required=True)
    """
        The JSON format version
    """

    width = marshmallow.fields.Int(required=True)
    """
        Number of tile columns
    """

    @marshmallow.post_load
    def load_map(self, item, many, **kwargs):
        """
            Called automatically to load the map into memory.
        """
        perform_post_load = True if "performPostLoad" not in self.context.keys() else self.context["performPostLoad"]
        if perform_post_load:
            if "backgroundcolor" in item.keys():
                item["backgroundcolor"] = objects.Color.from_hex(hex=item["backgroundcolor"])
        return item

    @marshmallow.post_dump
    def dump_map(self, data, many, **kwargs):
        """
            Called automatically to export the map from memory.
        """
        perform_post_dump = True if "performPostDump" not in self.context.keys() else self.context["performPostDump"]
        if perform_post_dump:
            if "backgroundcolor" in data.keys():
                data["backgroundcolor"] = str(data["backgroundcolor"])
        return data

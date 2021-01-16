import marshmallow

from . import constants, terrain, tile, objects

class TileSet(marshmallow.Schema):
    backgroundcolor = marshmallow.fields.Str(required=True)
    """
        Hex-formatted color (#RRGGBB or #AARRGGBB) (optional)
    """

    columns = marshmallow.fields.Int(required=True)
    """
        The number of tile columns in the tileset
    """

    firstgid = marshmallow.fields.Int(required=True)
    """
        GID corresponding to the first tile in the set
    """

    grid = marshmallow.fields.Str(required=False)
    """
        (optional)
    """

    image = marshmallow.fields.Str(required=True)
    """
        Image used for tiles in this set
    """

    imageheight = marshmallow.fields.Int(required=True)
    """
        Height of source image in pixels
    """

    imagewidth = marshmallow.fields.Int(required=True)
    """
        Width of source image in pixels
    """

    margin = marshmallow.fields.Int(required=True)
    """
        Buffer between image edge and first tile (pixels)
    """

    name = marshmallow.fields.Str(required=True)
    """
        Name given to this tileset
    """

    objectalignment = marshmallow.fields.Str(required=True, validate=marshmallow.validate.OneOf(choices=[
        constants.Alignment.unspecified.value,
        constants.Alignment.topleft.value,
        constants.Alignment.top.value,
        constants.Alignment.topright.value,
        constants. Alignment.left.value,
        constants.Alignment.center.value,
        constants. Alignment.right.value,
        constants.Alignment.bottomleft.value,
        constants.Alignment.bottom.value,
        constants. Alignment.bottomright.value
    ]))
    """
        Alignment to use for tile objects (unspecified (default), topleft, top, topright, left, center, right, bottomleft, bottom or bottomright) (since 1.4)
    """

    properties = marshmallow.fields.List(marshmallow.fields.Dict(), required=True)
    """
        Array of :ref:`Properties <json-property>`
    """

    source = marshmallow.fields.Str(required=True)
    """
        The external file that contains this tilesets data
    """

    spacing = marshmallow.fields.Int(required=True)
    """
        Spacing between adjacent tiles in image (pixels)
    """

    terrains = marshmallow.fields.List(marshmallow.fields.Nested(terrain.Terrain), required=False)
    """
        Array of :ref:`Terrains <json-terrain>` (optional)
    """

    tilecount = marshmallow.fields.Int(required=True)
    """
        The number of tiles in this tileset
    """

    tiledversion = marshmallow.fields.Str(required=True)
    """
        The Tiled version used to save the file
    """

    tileheight = marshmallow.fields.Int(required=True)
    """
        Maximum height of tiles in this set
    """

    tileoffset = marshmallow.fields.Int(required=False)
    """
        (optional)
    """

    tiles = marshmallow.fields.List(marshmallow.fields.Nested(tile.Tile), required=False)

    @marshmallow.post_load
    def load_tileset(self, item, many, **kwargs):
        """
            Called automatically to load the tileset into memory.
        """
        perform_post_load = True if "performPostLoad" not in self.context.keys() else self.context["performPostLoad"]
        if perform_post_load:
            item["backgroundcolor"] = objects.Color.from_hex(hex=item["backgroundcolor"])
        return item

    @marshmallow.post_dump
    def dump_tileset(self, data, many, **kwargs):
        """
            Called automatically to export the tileset from memory.
        """
        perform_post_dump = True if "performPostDump" not in self.context.keys() else self.context["performPostDump"]
        if perform_post_dump:
            data["backgroundcolor"] = str(data["backgroundcolor"])
        return data

import zlib
import json
import gzip
import base64

# Optionally import zstd - if we can't find it then mark it and raise an error if we try to use it
try:
    import zstd
except ModuleNotFoundError:
    zstd = None
import marshmallow

from . import constants, chunk, object

class Layer(marshmallow.Schema):
    chunks = marshmallow.fields.List(marshmallow.fields.Nested(chunk.Chunk))
    """
        Array of :ref:`chunks <json-chunk>` (optional). tilelayer only.
    """

    compression = marshmallow.fields.Str(required=False, default="", validate=marshmallow.validate.OneOf(choices=[
        constants.Compression.zlib.value,
        constants.Compression.gzip.value,
        constants.Compression.none.value,
        constants.Compression.zstd.value
    ]))
    """
        zlib, gzip, zstd (since Tiled 1.3) or empty (default). tilelayer only.
    """

    data = marshmallow.fields.Field(required=True)
    """
        Array of unsigned int (GIDs) or base64-encoded data. tilelayer only.
    """

    draworder = marshmallow.fields.Str(required=False, validate=marshmallow.validate.OneOf(choices=[
        constants.DrawOrder.index.value,
        constants.DrawOrder.topdown.value
    ]))
    """
        topdown (default) or index. objectgroup only.
    """

    encoding = marshmallow.fields.Str(required=False, validate=marshmallow.validate.OneOf(choices=[
        constants.Encoding.csv.value,
        constants.Encoding.base64.value
    ]))
    """
        csv (default) or base64. tilelayer only.
    """

    height = marshmallow.fields.Int(required=True)
    """
        Row count. Same as map height for fixed-size maps.
    """

    id = marshmallow.fields.Int(required=True)
    """
        Incremental ID - unique across all layers
    """

    image = marshmallow.fields.Str(required=False)
    """
        Image used by this layer. imagelayer only.
    """

    layers = marshmallow.fields.List(marshmallow.fields.Nested(lambda: Layer()))

    name = marshmallow.fields.Str(required=True)
    """
        Name assigned to this layer
    """

    objects = marshmallow.fields.List(marshmallow.fields.Nested(object.Object))
    """
        Array of :ref:`objects <json-object>`. objectgroup only.
    """

    offsetx = marshmallow.fields.Float(required=False, default=0)
    """
        Horizontal layer offset in pixels (default: 0)
    """

    offsety = marshmallow.fields.Float(required=False, default=0)
    """
        Vertical layer offset in pixels (default: 0)
    """

    opacity = marshmallow.fields.Float(required=True, validate=lambda value: value >= 0 <= 1)
    """
        Value between 0 and 1
    """

    parallaxx = marshmallow.fields.Float(required=False, default=1.0)
    """
        Horizontal :ref:`parallax factor <parallax-factor>` for this layer (default: 1). (since Tiled 1.5)
    """

    parallaxy = marshmallow.fields.Float(required=False, default=1.0)
    """
        Vertical :ref:`parallax factor <parallax-factor>` for this layer (default: 1). (since Tiled 1.5)
    """

    properties = marshmallow.fields.List(marshmallow.fields.Dict(), required=False, default=[])
    """
        Array of :ref:`Properties <json-property>`
    """

    startx = marshmallow.fields.Int(required=False)
    """
        X coordinate where layer content starts (for infinite maps)
    """

    starty = marshmallow.fields.Int(required=False)
    """
        Y coordinate where layer content starts (for infinite maps)
    """

    tintcolor = marshmallow.fields.Str(required=False)
    """
        Hex-formatted :ref:`tint color <tint-color>` (#RRGGBB or #AARRGGBB) that is multiplied with any graphics drawn by this layer or any child layers (optional).
    """

    transparentcolor = marshmallow.fields.Str(required=False)
    """
        Hex-formatted color (#RRGGBB) (optional). imagelayer only.
    """

    type = marshmallow.fields.Str(required=True, validate=marshmallow.validate.OneOf(choices=[
        constants.Type.group.value,
        constants.Type.tilelayer.value,
        constants.Type.objectgroup.value,
        constants.Type.imagelayer.value
    ]))
    """
        tilelayer, objectgroup, imagelayer or group
    """

    visible = marshmallow.fields.Boolean(required=True)
    """
        Whether layer is shown or hidden in editor
    """

    width = marshmallow.fields.Int(required=True)
    """
        Column count. Same as map width for fixed-size maps.
    """

    x = marshmallow.fields.Int(required=True, default=0)
    """
        Horizontal layer offset in tiles. Always 0.
    """

    y = marshmallow.fields.Int(required=True, default=0)
    """
        Vertical layer offset in tiles. Always 0.
    """

    @marshmallow.post_load
    def load_layer(self, item, many, **kwargs):
        """
            Called automatically to load the tileset into memory.
        """
        perform_post_load = True if "performPostLoad" not in self.context.keys() else self.context["performPostLoad"]
        if perform_post_load:
            if "tintcolor" in item.keys():
                item["tintcolor"] = objects.Color.from_hex(hex=item["tintcolor"])
            if "transparentcolor" in item.keys():
                item["transparentcolor"] = objects.Color.from_hex(hex=item["transparentcolor"])

            # Load compressed data if necessary
            compression = constants.Compression.none.value if "compression" not in item.keys() else item["compression"]
            if compression == constants.Compression.zlib.value:
                in_data = base64.b64decode(item["data"])
                in_data = zlib.decompress(in_data).decode("utf-8")
                item["data"] = json.loads(in_data)
            elif compression == constants.Compression.gzip.value:
                in_data = base64.b64decode(item["data"])
                in_data = gzip.decompress(in_data).decode("utf-8")
                item["data"] = json.loads(in_data)
            elif compression == constants.Compression.zstd.value:
                if zstd is None:
                    raise ModuleNotFoundError("Library zstd not installed: https://pypi.org/project/zstd/")
                in_data = base64.b64decode(item["data"])
                in_data = zstd.decompress(in_data).decode("utf-8")
                item["data"] = json.loads(in_data)
            elif compression == constants.Compression.none.value:
                pass
            else:
                raise ValueError("Unsupported compression type: %s" % item["compression"])
        return item

    @marshmallow.post_dump
    def dump_layer(self, data, many, **kwargs):
        """
            Called automatically to export the tileset from memory.
        """
        perform_post_dump = True if "performPostDump" not in self.context.keys() else self.context["performPostDump"]
        if perform_post_dump:
            if "tintcolor" in data.keys():
                data["tintcolor"] = str(data["tintcolor"])
            if "transparentcolor" in data.keys():
                data["transparentcolor"] = str(data["transparentcolor"])

            # Load compressed data if necessary
            compression = constants.Compression.none.value if "compression" not in data.keys() else data["compression"]
            if compression == constants.Compression.zlib.value:
                out_data = json.dumps(data["data"]).encode("utf-8")
                out_data = zlib.compress(out_data)
                out_data = base64.b64encode(out_data)
                data["data"] = out_data.decode("utf-8")
            elif compression == constants.Compression.gzip.value:
                out_data = json.dumps(data["data"]).encode("utf-8")
                out_data = gzip.compress(out_data)
                out_data = base64.b64encode(out_data)
                data["data"] = out_data.decode("utf-8")
            elif compression == constants.Compression.zstd.value:
                if zstd is None:
                    raise ModuleNotFoundError("Library zstd not installed: https://pypi.org/project/zstd/")
                out_data = json.dumps(data["data"]).encode("utf-8")
                out_data = zstd.compress(out_data)
                out_data = base64.b64encode(out_data)
                data["data"] = out_data.decode("utf-8")
            elif compression == constants.Compression.none.value:
                pass
            else:
                raise ValueError("Unsupported compression type: %s" % item["compression"])
        return data

# pytiled

This library implements support for loading pytiled map data exported in the JSON format.

## Installation

```bash
sudo python3 setup.py install
```
## Usage

Reference https://github.com/mapeditor/tiled/blob/master/docs/reference/json-map-format.rst for documentation on the JSON structures returned.

```python
import tiled

with open("myMap.json", "r") as handle:
    payload = handle.read()

map_schema = tiled.map.Map()
map_data = map_schema.loads(payload)

# Data is verified by marshmallow, compression is handled & colors parsed
print(map_data)
```

## Contexts

### performPostLoad

Whether or not to perform post load functions such as processing compression.

```python
import tiled

with open("myMap.json", "r") as handle:
    payload = handle.read()

map_schema = tiled.map.Map()
map_schema.context = {"performPostLoad": False}
map_data = map_schema.loads(payload)

# Data is returned unmolested
print(map_data)
```

### performPostDump

Whether or not post dump processing is ran.

```python
import tiled

map_schema = tiled.map.Map()
map_schema.context = {"performPostDump": False}
output_map_Data = map_schema.dumps(payload)

# Data is written without post dump unmolested
print(map_data)
```

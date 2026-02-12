# Example 03: Modify StruXML File

This example demonstrates how to programmatically modify FEM-Design models by working directly with the StruXML format.

## Files in This Example

- **03_modify_struxml.py** - Modify existing model elements
- **03b_create_objects.py** - Create new objects from scratch
- **concrete_beam.struxml** - Input model file
- **README.md** - This documentation

## What This Example Does

### Example 03: Modify Existing Elements

1. **Deserializes** a `.struxml` file into Python objects using xsdata
2. **Extracts information** about load cases and load combinations
3. **Modifies load case names** (e.g., "DL" → "DeadLoad")
4. **Modifies load combination names** (e.g., "ULS_1" → "ULS - Ultimate Limit State")
5. **Modifies beam properties** (name and color attributes)
6. **Serializes** the modified model back to a `.struxml` file
7. **Opens** the modified file in FEM-Design using FemDesignConnection

### Example 03b: Create Objects from Scratch

1. **Creates new load cases** using strusoft25.py dataclasses
2. **Creates new load combinations** with specified factors
3. **Adds new objects** to an existing model
4. **Demonstrates** how to use the strusoft25 classes directly
5. **Generates GUIDs** for new elements
6. **Uses enums** for type and property values

## Key Concepts

### StruXML Structure

StruXML files are XML-based model files that can be edited programmatically. The main components are:

- **Database**: Root structure containing all model data
- **Entities**: Contains structural elements like bars, slabs, supports, and loads
- **Sections**: Cross-section definitions
- **Materials**: Material property definitions

### XSData Classes

The FemDesign Python API uses [xsdata](https://xsdata.readthedocs.io/) to parse StruXML files into Python dataclasses. Key classes used in this example:

- **Database**: Main container (`from femdesign.strusoft.interop.struxml.data.strusoft25`)
- **LoadCaseType**: Represents individual load cases
- **LoadCombinationType**: Represents load combinations
- **BarType**: Represents bars (beams, columns, trusses)

### Accessing Model Data

```python
# Load a model
database = deserialize_from_filepath("model.struxml")

# Access load cases
for load_case in database.entities.loads.load_case:
    print(load_case.name, load_case.type_value)

# Access load combinations
for load_comb in database.entities.loads.load_combination:
    print(load_comb.name, load_comb.load_case)

# Access bars (beams)
for bar in database.entities.bar:
    print(bar.name, bar.type_value)
```

### Modifying Model Data

After deserializing, you can modify the Python objects directly:

```python
# Modify load case name
database.entities.loads.load_case[0].name = "NewName"

# Modify bar name
database.entities.bar[0].name = "Beam_001"

# Add attributes (like color)
database.entities.bar[0].any_attributes["color"] = "#FF0000"
```

### Saving Changes

Save the modified model back to a `.struxml` file:

```python
serialize_to_struxml(database, filepath="modified_model.struxml")
```

## Running the Examples

**Modify existing elements:**
```bash
cd examples/03_modify_struxml
python 03_modify_struxml.py
```

**Create new objects:**
```bash
cd examples/03_modify_struxml
python 03b_create_objects.py
```

## Expected Output

The script will:

1. Display original load cases and bars
2. Show the modifications being made
3. Display the modified load cases and bars
4. Save a new file: `concrete_beam_modified.struxml`
5. Open it in FEM-Design
6. Save it as `concrete_beam_modified_analyzed.str`

## Use Cases

This approach is useful for:
Creating Objects from Scratch

**Yes, you CAN create objects using strusoft25.py classes!** They are part of the femdesign package.

### Quick Start Guide

```python
from femdesign.strusoft.interop.struxml.data.strusoft25 import (
    LoadCaseType,
    LoadcasetypeType,
    Loadcasedurationtype,
)
import uuid
from datetime import datetime

# Create a new load case
new_load_case = LoadCaseType(
    guid=str(uuid.uuid4()),           # Generate new GUID
    last_change=datetime.now(),       # Timestamp
    action="added",                   # Modification type
    name="Wind Load",                 # Name (max 80 chars)
    type_value=LoadcasetypeType.STATIC,           # Use enums!
    duration_class=Loadcasedurationtype.SHORT_TERM,
)

# Add to an existing model
database.entities.loads.load_case.append(new_load_case)
```

### Key Classes You Can Create

| Class | Import From | Purpose |
|-------|-------------|---------|
| `LoadCaseType` | strusoft25 | Load cases |
| `LoadCombinationType` | strusoft25 | Load combinations |
| `BarType` | strusoft25 | Beams, columns, trusses |
| `PointSupportType` | strusoft25 | Point supports |
| `LineLoadType` | strusoft25 | Line loads |
| `PointLoadType` | strusoft25 | Point loads |

### Important Tips for Creating Objects

1. **Always generate new GUIDs**: `str(uuid.uuid4())`
2. **Use enums for type fields**: Import enum types like `LoadcasetypeType`, `Loadcombtype`, etc.
3. **Use keyword arguments**: Dataclasses require keyword args
4. **Check required fields**: Look at the class definition to see which fields are required
5. **Set timestamps**: Use `datetime.now()` for `last_change` fields
6. **Set action**: Use "added" for new elements

### Example: Complete Object Creation

```python
from femdesign.strusoft.interop.struxml.data.strusoft25 import (
    LoadCombinationType,
    Loadcombtype,
    LoadCombinationLoadCaseType,
)

# Create load combination with multiple load cases
combination = LoadCombinationType(
    guid=str(uuid.uuid4()),
    last_change=datetime.now(),
    action="added",
    name="ULS - Ultimate",
    type_value=Loadcombtype.ULTIMATE_ORDINARY,
    load_case=[
        LoadCombinationLoadCaseType(guid="<dead-load-guid>", gamma=1.35),
        LoadCombinationLoadCaseType(guid="<live-load-guid>", gamma=1.5),
    ]
)
```

See **03b_create_objects.py** for a complete working example!

## Important Notes

- StruXML files can be opened and saved in FEM-Design (`.struxml` format)
- The `.str` format is binary and cannot be directly modified
- Always validate modified models in FEM-Design before analysis
- GUIDs should remain unchanged for existing elements
- When adding new elements, generate new GUIDs using `uuid.uuid4()`
- All strusoft25 classes are standard Python dataclasses generated by xsdata
## Important Notes

- StruXML files can be opened and saved in FEM-Design (`.struxml` format)
- The `.str` format is binary and cannot be directly modified
- Always validate modified models in FEM-Design before analysis
- GUIDs should remain unchanged for existing elements
- When adding new elements, generate new GUIDs using `uuid.uuid4()`

## Further Reading

- [xsdata documentation](https://xsdata.readthedocs.io/)
- StruXML schema: `strusoft25.xsd` in the project root
- FemDesign API documentation: [FEM-Design API](https://strusoft.com/fem-design-api)

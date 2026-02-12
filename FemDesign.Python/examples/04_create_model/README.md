# Example 04: Create Model from Scratch

This example demonstrates how to programmatically create a complete FEM-Design model from scratch using Python dataclasses.

## Files in This Example

- **create_model.py** - Creates a new model with a point support
- **model.struxml** - Output model file (generated)
- **README.md** - This documentation

## What This Example Does

1. **Creates an empty Database** object with required metadata (GUID, timestamps, version)
2. **Creates a point support** at coordinates (10, 10, 10) with spring rigidity of 100000 kN/m
3. **Configures support rigidity** using RigidityDataType2 with separate motion and rotation stiffnesses
4. **Adds the support to the model** by creating the entities structure
5. **Serializes** the complete model to a `.struxml` file
6. **Opens** the model in FEM-Design using FemDesignConnection
7. **Detaches** the connection to allow manual interaction

## Key Concepts

### Creating a Database from Scratch

Every FEM-Design model starts with a `Database` object that contains required metadata:

```python
model = Database(
    end=EmptyType(),                                    # Required end marker
    struxml_version="01.00.000",                        # Format: XX.XX.XXX
    source_software="FemDesign API Python",             # Software identifier
    start_time=XmlDateTime.from_datetime(datetime.now()),  # Creation time
    end_time=XmlDateTime.from_datetime(datetime.now()),    # Modification time
    guid=str(uuid.uuid4()),                             # Unique identifier
    country=Eurocodetype.COMMON,                        # Standard/country code
)
```

### Creating a Point Support

Point supports require position and rigidity definition:

```python
point_support = PointSupportType(
    position=PointType3D(x=10.0, y=10.0, z=10.0),      # 3D coordinates
    group=SupportRigidityDataType.Group(
        local_x=PointType3D(x=1.0, y=0.0, z=0.0),      # Local coordinate system
        local_y=PointType3D(x=0.0, y=1.0, z=0.0),
        rigidity=RigidityDataType2(
            motions=StiffnessType(                      # Translation springs
                x_neg=100000.0, x_pos=100000.0,
                y_neg=100000.0, y_pos=100000.0,
                z_neg=100000.0, z_pos=100000.0
            ),
            rotations=StiffnessType(                    # Rotation springs
                x_neg=0.0, x_pos=0.0,                   # 0 = free rotation
                y_neg=0.0, y_pos=0.0,
                z_neg=0.0, z_pos=0.0
            )
        )
    ),
    guid=str(uuid.uuid4()),
    last_change=XmlDateTime.from_datetime(datetime.now()),
    action=ModificationType.ADDED,
    name="S1",
)
```

### Building the Model Structure

Add entities to the model by creating the nested structure:

```python
model.entities = Database.Entities(
    supports=Database.Entities.Supports(
        point_support=[point_support]
    )
)
```

### Saving and Opening the Model

```python
# Save to file
serialize_to_struxml(model, True, OUTPUT_MODEL)

# Open in FEM-Design
connection = FemDesignConnection(minimized=False)
connection.Open(OUTPUT_MODEL)
connection.Detach()
```

## Running the Example

```bash
cd examples/04_create_model
python create_model.py
```

## Expected Output

The script will:

1. Create an empty Database object
2. Create a point support with specified rigidity
3. Display model information:
   - Model GUID
   - Point support position (10.0, 10.0, 10.0)
   - Rigidity value (100000.0)
4. Save the model as `model.struxml`
5. Open the model in FEM-Design
6. Detach the connection

## Key Classes Used

| Class | Purpose |
|-------|---------|
| `Database` | Root container for the entire model |
| `EmptyType` | Required end marker for Database |
| `PointSupportType` | Point support definition |
| `PointType3D` | 3D point coordinates |
| `SupportRigidityDataType.Group` | Support rigidity with local coordinate system |
| `RigidityDataType2` | Rigidity definition with motions and rotations |
| `StiffnessType` | Spring stiffness values in 3 directions |
| `ModificationType` | Enum for element action (ADDED, MODIFIED) |
| `Eurocodetype` | Enum for country/standard codes |

## Use Cases

This approach is useful for:

- **Parametric model generation**: Create models based on parameters
- **Automated design**: Generate multiple design variants programmatically
- **Integration with other tools**: Connect Python workflows to FEM-Design
- **Batch processing**: Create multiple models with different configurations
- **Research and optimization**: Generate models for parametric studies

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
**GUIDs are required**: Every element needs a unique GUID generated with `uuid.uuid4()`
- **Timestamps are required**: Use `XmlDateTime.from_datetime(datetime.now())` for time fields
- **Local coordinate system**: Point supports with Group rigidity need `local_x` and `local_y` vectors
- **Rigidity definition**: Use `RigidityDataType2` with `motions` and `rotations` for complete support definition
- **StiffnessType**: Requires both negative and positive direction values (e.g., `x_neg`, `x_pos`)
- **Action type**: New elements should have `action=ModificationType.ADDED`
- **Validation**: Always open and validate created models in FEM-Design before analysis

## Next Steps

To extend this example, you can add:

- **Bars (beams/columns)**: Using `BarType` with section and material references
- **Materials**: Using `Database.Materials` to define concrete, steel, etc.
- **Sections**: Using `Database.Sections` to define cross-sections
- **Load cases**: Using `LoadCaseType` for dead load, live load, etc.
- **Loads**: Using `PointLoadType`, `LineLoadType`, or `SurfaceLoadType`
- **Slabs**: Using `SlabType` for floor/wall panels

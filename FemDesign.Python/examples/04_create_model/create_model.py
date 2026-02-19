"""
Example 3: Modify StruXML File
===============================
This example demonstrates how to:
- Deserialize (read) a .struxml file into Python objects
- Extract information like load cases and load combinations
- Modify load case names
- Modify beam names and properties
- Serialize back to .struxml file
- Open the modified file with FemDesignConnection
"""

import os

from femdesign.comunication import *
from femdesign.calculate import *
from femdesign.interop import *
from femdesign.io import *


# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to save the model
OUTPUT_MODEL = os.path.join(SCRIPT_DIR, "model.struxml")

def main():
    """Main function to demonstrate the model creation."""
    # Create an empty database
    model = Database(
        end=EmptyType(),
        struxml_version="01.00.000",  # Format: XX.XX.XXX
        source_software="FemDesign API Python",
        start_time=XmlDateTime.from_datetime(datetime.now()),
        end_time=XmlDateTime.from_datetime(datetime.now()),
        guid=str(uuid.uuid4()),
        # Optional fields with defaults:
        country=Eurocodetype.COMMON,
        # soil_as_solid=False,
        # convertid="00000000-0000-0000-0000-000000000000"
    )

    # Create a point support at (10, 10, 10) with rigidity 100000
    point_support = PointSupportType(
        position=PointType3D(x=10.0, y=10.0, z=10.0),
        group=SupportRigidityDataType.Group(
            local_x=PointType3D(x=1.0, y=0.0, z=0.0),  # Local X axis direction
            local_y=PointType3D(x=0.0, y=1.0, z=0.0),  # Local Y axis direction
            rigidity=RigidityDataType2(
                motions=StiffnessType(
                    x_neg=100000.0, x_pos=100000.0,
                    y_neg=100000.0, y_pos=100000.0,
                    z_neg=100000.0, z_pos=100000.0
                ),
                rotations=StiffnessType(
                    x_neg=0.0, x_pos=0.0,
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

    # Add the point support to the model
    model.entities = Database.Entities(
        supports=Database.Entities.Supports(
            point_support=[point_support]
        )
    )

    serialize_to_struxml(model, True, OUTPUT_MODEL)

    print("Model created successfully!")
    print(f"Model GUID: {model.guid}")
    print(f"Point support created at position: ({point_support.position.x}, {point_support.position.y}, {point_support.position.z})")
    if point_support.group and point_support.group.rigidity:
        print(f"Rigidity: {point_support.group.rigidity.motions.x_pos}")

    # Open the model in FEM-Design
    connection = FemDesignConnection(minimized=False)
    connection.Open(OUTPUT_MODEL)
    connection.Detach()  # Detach the connection to allow manual interaction with FEM-Design after opening the model
    

if __name__ == "__main__":
    main()

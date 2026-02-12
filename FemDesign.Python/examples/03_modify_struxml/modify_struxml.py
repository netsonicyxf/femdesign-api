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

# Path to the input model file
INPUT_MODEL = os.path.join(SCRIPT_DIR, "concrete_beam.struxml")
# Path to save the modified model
MODIFIED_MODEL = os.path.join(SCRIPT_DIR, "concrete_beam_modified.struxml")
# Path to save the analyzed model
OUTPUT_MODEL = os.path.join(SCRIPT_DIR, "concrete_beam_modified_analyzed.str")


def print_load_information(database: Database):
    """Print information about load cases and load combinations."""
    
    if not database.entities or not database.entities.loads:
        print("No loads found in the model")
        return
    
    loads = database.entities.loads
    
    # Print load cases
    print("\n" + "=" * 60)
    print("LOAD CASES")
    print("=" * 60)
    if loads.load_case:
        for i, load_case in enumerate(loads.load_case, 1):
            print(f"\n{i}. Name: {load_case.name}")
            print(f"   GUID: {load_case.guid}")
            print(f"   Type: {load_case.type_value.value}")
            print(f"   Duration Class: {load_case.duration_class.value}")
    else:
        print("No load cases found")
    
    # Print load combinations
    print("\n" + "=" * 60)
    print("LOAD COMBINATIONS")
    print("=" * 60)
    if loads.load_combination:
        for i, load_comb in enumerate(loads.load_combination, 1):
            print(f"\n{i}. Name: {load_comb.name}")
            print(f"   GUID: {load_comb.guid}")
            print(f"   Type: {load_comb.type_value.value}")
            print(f"   Contains {len(load_comb.load_case)} load case(s):")
            for lc in load_comb.load_case:
                print(f"     - GUID: {lc.guid}, Factor: {lc.gamma}")
    else:
        print("No load combinations found")


def print_bar_information(database: Database):
    """Print information about bars (beams, columns, etc.)."""
    
    if not database.entities or not database.entities.bar:
        print("No bars found in the model")
        return
    
    print("\n" + "=" * 60)
    print("BARS (Beams/Columns)")
    print("=" * 60)
    
    for i, bar in enumerate(database.entities.bar, 1):
        print(f"\n{i}. Name: {bar.name}")
        print(f"   GUID: {bar.guid}")
        print(f"   Type: {bar.type_value.value}")
        print(f"   Number of parts: {len(bar.bar_part)}")
        
        # Print any custom attributes (like color)
        if bar.any_attributes:
            print(f"   Custom attributes: {bar.any_attributes}")


def modify_load_cases(database : Database):
    """Modify load case names."""
    
    if not database.entities or not database.entities.loads:
        print("No loads to modify")
        return
    
    loads = database.entities.loads
    
    if loads.load_case:
        for load_case in loads.load_case:
            # Modify load case names
            if load_case.name == "DL":
                old_name = load_case.name
                load_case.name = "DeadLoad"
                print(f"\nModified load case: '{old_name}' -> '{load_case.name}'")
            elif load_case.name == "LL":
                old_name = load_case.name
                load_case.name = "LiveLoad"
                print(f"Modified load case: '{old_name}' -> '{load_case.name}'")


def modify_load_combinations(database : Database):
    """Modify load combination names."""
    
    if not database.entities or not database.entities.loads:
        print("No loads to modify")
        return
    
    loads = database.entities.loads
    
    if loads.load_combination:
        for load_comb in loads.load_combination:
            # Modify load combination name
            if load_comb.name == "ULS_1":
                old_name = load_comb.name
                load_comb.name = "ULS - Ultimate Limit State"
                print(f"Modified load combination: '{old_name}' -> '{load_comb.name}'")


def modify_bars(database : Database):
    """Modify bar names and add color attribute."""
    
    if not database.entities or not database.entities.bar:
        print("No bars to modify")
        return
    
    for bar in database.entities.bar:
        # Modify bar name
        if bar.name and bar.name.startswith("B."):
            old_name = bar.name
            bar.name = "Beam_Main_001"
            print(f"\nModified bar name: '{old_name}' -> '{bar.name}'")
            
            # Add a color attribute (RGB color in hex format without #, e.g. FF0000 for red)
            # Red color: FF0000
            bar.bar_part[0].colouring = EntityColor(tone="FF0000")
            print(f"Added color attribute: {bar.bar_part[0].colouring.tone} to bar '{bar.name}'")


def main():
    print("=" * 60)
    print("STRUXML MODIFICATION EXAMPLE")
    print("=" * 60)
    
    # Step 1: Deserialize the struxml file
    print(f"\nStep 1: Reading model from {INPUT_MODEL}")
    database = deserialize_from_filepath(INPUT_MODEL)
    print("✓ Model loaded successfully")
    
    # Step 2: Print current information
    print("\n" + "▬" * 60)
    print("ORIGINAL MODEL INFORMATION")
    print("▬" * 60)
    print_load_information(database)
    print_bar_information(database)
    
    # Step 3: Modify the model
    print("\n" + "▬" * 60)
    print("MODIFYING MODEL")
    print("▬" * 60)
    modify_load_cases(database)
    modify_load_combinations(database)
    modify_bars(database)
    
    # Step 4: Print modified information
    print("\n" + "▬" * 60)
    print("MODIFIED MODEL INFORMATION")
    print("▬" * 60)
    print_load_information(database)
    print_bar_information(database)
    
    # Step 5: Serialize back to struxml
    print(f"\nStep 5: Saving modified model to {MODIFIED_MODEL}")
    serialize_to_struxml(database, filepath=MODIFIED_MODEL)
    print("✓ Modified model saved successfully")
    
    # Step 6: Open in FEM-Design and run analysis
    print(f"\nStep 6: Opening modified model in FEM-Design")
    connection = FemDesignConnection(minimized=True)
    
    try:
        connection.SetVerbosity(Verbosity.SCRIPT_LOG_LINES)
        
        # Open the modified model
        connection.Open(MODIFIED_MODEL)
        print("✓ Model opened in FEM-Design")
        
        # You can run analysis here if needed
        # from femdesign.calculate.analysis import Analysis
        # static_analysis = Analysis.StaticAnalysis()
        # connection.RunAnalysis(static_analysis)
        
        # Save to demonstrate it works
        connection.Save(OUTPUT_MODEL)
        print(f"✓ Model saved to: {OUTPUT_MODEL}")
        
        connection.Detach()
        
        print("\n" + "=" * 60)
        print("SUCCESS!")
        print("=" * 60)
        print("1. Notice the updated load case/combination names")
        print("2. Check the beam properties for the updated name")
        
    except Exception as err:
        print(f"\n✗ Error occurred: {err}")
        connection.KillProgramIfExists()
        raise err


if __name__ == "__main__":
    main()

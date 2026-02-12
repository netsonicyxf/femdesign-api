"""
Example 2: Basic Eigenfrequency Analysis
=========================================
This example demonstrates how to perform eigenfrequency (modal) analysis
to calculate natural frequencies and mode shapes of a structure.
"""

import os
from femdesign.comunication import FemDesignConnection, Verbosity
from femdesign.calculate.analysis import Analysis

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the FEM-Design model file in the same folder
MODEL_PATH = os.path.join(SCRIPT_DIR, "concrete_beam.struxml")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "concrete_beam_frequencies.str")

def main():
    # Create a connection to FEM-Design
    connection = FemDesignConnection(minimized=True)
    
    try:
        # Set verbosity to see script execution details
        connection.SetVerbosity(Verbosity.SCRIPT_LOG_LINES)
        
        # Open the model file
        print(f"Opening model: {MODEL_PATH}")
        connection.Open(MODEL_PATH)
        
        # Create eigenfrequency analysis configuration
        # num_shapes: Number of mode shapes to calculate (default: 5)
        # The analysis will find the first 5 natural frequencies and mode shapes
        print("Running eigenfrequency analysis...")
        freq_analysis = Analysis.FrequencyAnalysis(num_shapes=5)
        
        # Run the eigenfrequency analysis
        connection.RunAnalysis(freq_analysis)
        
        # Save the results to a new file
        print(f"Saving results to: {OUTPUT_PATH}")
        connection.Save(OUTPUT_PATH)
        
        print("\nEigenfrequency analysis completed successfully!")
        print(f"Output saved to: {OUTPUT_PATH}")
        print("\nYou can now open the output file in FEM-Design to:")
        print("  - View natural frequencies in the Results tab")
        print("  - Visualize mode shapes")
        print("  - Check modal participation factors")
        
        # Close FEM-Design
        connection.Exit()
        
    except Exception as err:
        # If something goes wrong, make sure to kill the FEM-Design process
        print(f"Error occurred: {err}")
        connection.KillProgramIfExists()
        raise err

if __name__ == "__main__":
    main()

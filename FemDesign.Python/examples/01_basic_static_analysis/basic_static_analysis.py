"""
Example 1: Basic Static Analysis
=================================
This example demonstrates how to open a FEM-Design model,
run a simple static analysis, and save the results.
"""

import os
from femdesign.comunication import FemDesignConnection, Verbosity
from femdesign.calculate.analysis import Analysis

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the FEM-Design model file in the same folder
MODEL_PATH = os.path.join(SCRIPT_DIR, "concrete_beam.struxml")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "concrete_beam_analyzed.str")

def main():
    # Create a connection to FEM-Design
    # Set minimized=True to run FEM-Design in minimized mode
    connection = FemDesignConnection(minimized=False)
    
    try:
        # Set verbosity to see what's happening
        # SCRIPT_LOG_LINES will show script execution details
        connection.SetVerbosity(Verbosity.SCRIPT_LOG_LINES)
        
        # Open the model file
        print(f"Opening model: {MODEL_PATH}")
        connection.Open(MODEL_PATH)
        
        # Create a static analysis configuration
        # calcCase=True: Calculate load cases
        # calcComb=True: Calculate load combinations
        static_analysis = Analysis.StaticAnalysis()
        
        # Run the analysis
        print("Running static analysis...")
        connection.RunAnalysis(static_analysis)
        
        # Save the results to a new file
        print(f"Saving results to: {OUTPUT_PATH}")
        connection.Save(OUTPUT_PATH)
        
        print("\nAnalysis completed successfully!")
        print(f"Output saved to: {OUTPUT_PATH}")
        
        # Close FEM-Design
        connection.Detach()
        
    except Exception as err:
        # If something goes wrong, make sure to kill the FEM-Design process
        print(f"Error occurred: {err}")
        connection.KillProgramIfExists()
        raise err

if __name__ == "__main__":
    main()

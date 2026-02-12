# Example 1: Basic Static Analysis

This example demonstrates the fundamental workflow for running a static analysis in FEM-Design using Python.

## Contents

- `01_basic_static_analysis.py` - Python script to run static analysis
- `concrete_beam.struxml` - Sample FEM-Design model (reinforced concrete beam)

## What This Example Does

1. Opens a concrete beam model
2. Runs static analysis (calculates load cases and combinations)
3. Saves the analyzed model with results

## Model Description

The sample model is a 6m simply supported reinforced concrete beam with:
- Material: C40/50 concrete
- Section: 350×600 mm rectangular
- Reinforcement: 4×Ø16mm longitudinal bars, Ø8mm stirrups
- Loading: 10 kN/m distributed load
- Support: Pinned at both ends

## How to Run

```bash
cd examples/01_basic_static_analysis
python 01_basic_static_analysis.py
```

## Expected Output

The script will create a new file `concrete_beam_analyzed.str` in this folder containing the analysis results. You can open this file in FEM-Design to view:
- Reactions at supports
- Internal forces (shear, moment)
- Deflections

## Requirements

- FEM-Design installed and licensed
- Python 3.x
- femdesign Python package
- pywin32

## Next Steps

After running this example, check out:
- **Example 02**: Eigenfrequency analysis
- Modify the model path to analyze your own structures

# Example 2: Basic Eigenfrequency Analysis

This example demonstrates how to perform modal analysis (eigenfrequency analysis) to determine natural frequencies and mode shapes.

## Contents

- `02_eigen_freq_analysis.py` - Python script to run eigenfrequency analysis
- `concrete_beam.struxml` - Sample FEM-Design model (reinforced concrete beam)

## What This Example Does

1. Opens a concrete beam model
2. Runs eigenfrequency analysis to find the first 5 natural frequencies
3. Saves the model with frequency analysis results

## Natural Frequency Analysis

Eigenfrequency analysis determines:
- **Natural frequencies** - Frequencies at which the structure naturally vibrates
- **Mode shapes** - The deformation patterns at each natural frequency
- **Modal participation factors** - How much each mode contributes to the overall response

This is important for:
- Dynamic analysis
- Vibration assessment
- Seismic design
- Footfall analysis

## How to Run

```bash
cd examples/02_eigen_freq_analysis
python 02_eigen_freq_analysis.py
```

## Expected Output

The script will create `concrete_beam_frequencies.str` containing:
- First 5 natural frequencies and periods
- Mode shapes (visualizable in FEM-Design)
- Mass participation factors

Open the output file in FEM-Design and navigate to:
- **Results → Eigenfrequencies** to view frequencies and periods
- **Results → Mode shapes** to animate the vibration modes

## Configuration Options

You can modify the analysis by changing parameters in the script:

```python
# Calculate 10 mode shapes instead of 5
freq_analysis = Analysis.FrequencyAnalysis(num_shapes=10)

# Use different normalization (Unit instead of MassMatrix)
from femdesign.calculate.analysis import Freq
freq_analysis = Analysis.FrequencyAnalysis(
    num_shapes=5,
    norm_unit=Freq.ShapeNormalization.Unit
)
```

## Requirements

- FEM-Design installed and licensed
- Python 3.x
- femdesign Python package
- pywin32

## Learn More

- Example 01: Basic static analysis
- FEM-Design documentation on modal analysis

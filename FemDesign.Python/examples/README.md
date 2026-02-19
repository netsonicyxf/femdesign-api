# FemDesign Python API - Examples

This folder contains ready-to-run examples demonstrating various features of the FemDesign Python API. Each example is in its own folder with a complete, working model file.

## 📁 Folder Structure

Each example folder contains:

- **Python script** (`.py`) - The runnable example code
- **Model file** (`.struxml` or `.str`) - FEM-Design model for the example
- **README.md** - Detailed documentation for that specific example

```files
examples/
├── 01_basic_static_analysis/
│   ├── 01_basic_static_analysis.py
│   ├── concrete_beam.struxml
│   └── README.md
│
├── 02_eigen_freq_analysis/
│   ├── 02_eigen_freq_analysis.py
│   ├── concrete_beam.struxml
│   └── README.md
│
├── 03_modify_struxml/
│   ├── 03_modify_struxml.py
│   ├── concrete_beam.struxml
│   └── README.md
│
├── 04_create_model/
│   ├── create_model.py
│   ├── model.struxml (generated)
│   └── README.md
│
└── README.md (this file)
```

## 📚 Available Examples

### 01 - Basic Static Analysis

Learn the fundamental workflow:

- Opening FEM-Design models
- Running static analysis
- Saving results

**Use case**: Analyze a simply supported concrete beam under distributed load

### 02 - Eigenfrequency Analysis  

Perform modal analysis:

- Calculate natural frequencies
- Determine mode shapes
- View modal participation factors

**Use case**: Find vibration characteristics of the same concrete beam

### 03 - Modify StruXML File

Work with model files programmatically:

- Deserialize `.struxml` files into Python objects
- Read load cases and load combinations
- Modify element names and properties
- Add custom attributes (e.g., colors)
- Serialize back to `.struxml` format
- Open modified model in FEM-Design

**Use case**: Batch rename load cases, modify beam properties, and add visualization attributes

### 04 - Create Model from Scratch

Build complete FEM-Design models programmatically:

- Create empty Database object with required metadata
- Define point supports with spring rigidity
- Configure support rigidity using RigidityDataType2
- Build model structure with entities
- Serialize to `.struxml` format
- Open in FEM-Design

**Use case**: Parametric model generation, create a point support at (10, 10, 10) with 100000 kN/m rigidity

## 🚀 Quick Start

1. Navigate to any example folder:

   ```bash
   cd examples/01_basic_static_analysis
   ```

2. Run the Python script:

   ```bash
   python 01_basic_static_analysis.py
   ```

3. Check the output file(s) created in the same folder

4. Open the output in FEM-Design to view results

## 💡 Prerequisites

- **FEM-Design** installed with active license
- **Python 3.x**
- **femdesign Python package** installed
- **pywin32** package: `pip install pywin32`

## 📖 How to Use These Examples

### For Learning

1. Start with Example 01 to understand the basic workflow
2. Progress to Example 02 for different analysis types
3. Read the README.md in each folder for detailed explanations

### For Your Projects

1. Copy an example folder as a template
2. Replace the model file with your own `.str` or `.struxml`
3. Modify the script parameters as needed
4. Run and iterate

### Customization Tips

**Change the model file:**

```python
MODEL_PATH = os.path.join(SCRIPT_DIR, "your_model.str")
```

**Modify analysis settings:**

```python
# More mode shapes
freq_analysis = Analysis.FrequencyAnalysis(num_shapes=10)

# Different analysis options
static_analysis = Analysis.StaticAnalysis(calcCase=True, calcComb=True)
```

**Change output location:**
```python
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "results", "output.str")
```

## 🔧 Troubleshooting

**Script can't find the model file:**

- Make sure you're running the script from within its folder, OR
- The scripts use `os.path.dirname(os.path.abspath(__file__))` to find files relative to the script location

**FEM-Design doesn't start:**

- Verify FEM-Design is installed
- Check license is activated
- Ensure no other FEM-Design instances are running

**Import errors:**

- Install packages: `pip install pywin32`
- Verify femdesign package is in your Python path

**Analysis fails:**

- Open the model manually in FEM-Design first to check for errors
- Check the console output for detailed error messages
- Verify the model is valid and has necessary load cases/combinations

## 📝 File Formats

The examples work with both FEM-Design file formats:

- **`.struxml`** - XML-based format (human-readable, version control friendly)
- **`.str`** - Binary format (smaller file size)

You can use either format as input, and save to either format as output.

## 🔗 Additional Resources

- [FemDesign API Documentation](https://femdesign-api-docs.onstrusoft.com/docs/intro)
- [FemDesign Software](https://strusoft.com/software/3d-structural-analysis-software-fem-design/)
- Main repository examples: [FemDesign.Examples/Python](https://github.com/strusoft/femdesign-api/tree/master/FemDesign.Examples/Python)

## 🎯 Next Steps

After mastering these examples, explore:

- Creating custom analysis workflows
- Batch processing multiple models
- Extracting and post-processing results
- Integrating with other tools in your workflow

## 💬 Support

If you encounter issues:

1. Check the example's README.md for specific guidance
2. Review the FemDesign API documentation
3. Open an issue on the GitHub repository

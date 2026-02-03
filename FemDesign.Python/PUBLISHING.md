# Publishing FEM-Design to PyPI

## Prerequisites
1. Create a PyPI account at https://pypi.org/account/register/
2. Create a TestPyPI account at https://test.pypi.org/account/register/
3. Generate API tokens for both (recommended over password)
   - PyPI: https://pypi.org/manage/account/token/
   - TestPyPI: https://test.pypi.org/manage/account/token/

## Step 1: Test on TestPyPI (Recommended)

Upload to TestPyPI first to test the package:

```powershell
python -m twine upload --repository testpypi dist/*
```

When prompted:
- Username: __token__
- Password: (paste your TestPyPI API token, starts with pypi-...)

Then test installation from TestPyPI:
```powershell
pip install --index-url https://test.pypi.org/simple/ FEM-Design
```

## Step 2: Upload to PyPI (Production)

Once you've verified the package works on TestPyPI:

```powershell
python -m twine upload dist/*
```

When prompted:
- Username: __token__
- Password: (paste your PyPI API token, starts with pypi-...)

## Step 3: Verify Installation

Test that users can install your package:
```powershell
pip install FEM-Design
```

## Using API Tokens with .pypirc (Optional)

Create a file at %USERPROFILE%\.pypirc with:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-YourPyPITokenHere

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YourTestPyPITokenHere
```

This allows you to upload without entering credentials:
```powershell
python -m twine upload --repository testpypi dist/*
python -m twine upload dist/*
```

## Important Notes

- Make sure to increment the version number in pyproject.toml for each new release
- PyPI does not allow re-uploading the same version number
- Always test on TestPyPI before uploading to production PyPI
- The package name "FEM-Design" must be available on PyPI (check at https://pypi.org/project/FEM-Design/)
- Current version: 0.0.8

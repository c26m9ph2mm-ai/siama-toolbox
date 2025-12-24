# SIAMA Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Required Dependencies

The SIAMA application requires the following Python packages:

```
streamlit
pandas
plotly
numpy
scikit-learn
openpyxl (for Excel export)
```

## Installation Steps

### Option 1: Install All Dependencies at Once

```bash
pip install streamlit pandas plotly numpy scikit-learn openpyxl
```

Or if you prefer pip3:

```bash
pip3 install streamlit pandas plotly numpy scikit-learn openpyxl
```

### Option 2: Install from Requirements File

Create a `requirements.txt` file with the following content:

```
streamlit>=1.20.0
pandas>=1.5.0
plotly>=5.0.0
numpy>=1.19.0
scikit-learn>=1.2.0
openpyxl>=3.0.0
```

Then install:

```bash
pip install -r requirements.txt
```

## Verify Installation

Check if all packages are installed correctly:

```bash
python3 -c "import streamlit, pandas, plotly, numpy, sklearn; print('All packages installed successfully!')"
```

## Running the Application

### Navigate to Project Directory

```bash
cd /Users/sharmisthabanerjee/Desktop/siama
```

### Start the Application

```bash
streamlit run siama_app.py
```

Or specify a port:

```bash
streamlit run siama_app.py --server.port=8502
```

### Access the Application

Open your web browser and go to:
- **Default**: http://localhost:8501
- **Custom port**: http://localhost:8502

## Troubleshooting

### Issue: ModuleNotFoundError: No module named 'sklearn'

**Solution:**
```bash
pip3 install scikit-learn
```

Note: The package is called `scikit-learn` but imported as `sklearn`.

### Issue: ModuleNotFoundError: No module named 'streamlit'

**Solution:**
```bash
pip3 install streamlit
```

### Issue: Permission denied when installing packages

**Solution:** Use `--user` flag:
```bash
pip3 install --user streamlit pandas plotly numpy scikit-learn openpyxl
```

### Issue: Port already in use

**Solution:** Use a different port:
```bash
streamlit run siama_app.py --server.port=8503
```

Or kill the existing process:
```bash
pkill -f "streamlit run"
```

### Issue: Application won't start

**Check logs:**
```bash
streamlit run siama_app.py 2>&1 | tee streamlit.log
```

Review `streamlit.log` for error details.

## Package Versions (Tested)

The application has been tested with:

- Python: 3.9+
- streamlit: 1.20+
- pandas: 1.5+
- plotly: 5.0+
- numpy: 1.26+
- scikit-learn: 1.6+
- openpyxl: 3.0+

## System Requirements

### Minimum
- RAM: 2 GB
- Storage: 500 MB free
- OS: Windows 10+, macOS 10.14+, or Linux

### Recommended
- RAM: 4 GB
- Storage: 1 GB free
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Feature-Specific Dependencies

### For Manual Subgrouping
- streamlit
- pandas
- plotly

### For K-Means Clustering
- streamlit
- pandas
- plotly
- numpy
- scikit-learn ⭐ (required for automatic clustering)

### For Export Functionality
- pandas
- openpyxl (Excel export)
- json (built-in, for JSON export)

## Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

### Create Virtual Environment

```bash
# Navigate to project directory
cd /Users/sharmisthabanerjee/Desktop/siama

# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Install Dependencies in Virtual Environment

```bash
pip install streamlit pandas plotly numpy scikit-learn openpyxl
```

### Run Application in Virtual Environment

```bash
streamlit run siama_app.py
```

### Deactivate Virtual Environment

```bash
deactivate
```

## Updating Dependencies

To update all packages to latest versions:

```bash
pip install --upgrade streamlit pandas plotly numpy scikit-learn openpyxl
```

## Uninstallation

To remove all SIAMA dependencies:

```bash
pip uninstall streamlit pandas plotly numpy scikit-learn openpyxl
```

## Cloud Deployment (Optional)

### Streamlit Cloud

1. Push code to GitHub
2. Sign up at https://streamlit.io/cloud
3. Deploy from GitHub repository
4. Dependencies will be installed automatically from requirements.txt

### Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY siama_app.py .
COPY "SIAMA 3 (1).xlsm" .

EXPOSE 8501

CMD ["streamlit", "run", "siama_app.py"]
```

Build and run:

```bash
docker build -t siama-app .
docker run -p 8501:8501 siama-app
```

## Quick Start Summary

**Fastest way to get started:**

```bash
# Install dependencies
pip3 install streamlit pandas plotly numpy scikit-learn openpyxl

# Navigate to project
cd /Users/sharmisthabanerjee/Desktop/siama

# Run application
streamlit run siama_app.py
```

**Access at:** http://localhost:8501

---

## Support

If you encounter any installation issues:

1. Check Python version: `python3 --version`
2. Check pip version: `pip3 --version`
3. Verify package installation: `pip3 list | grep <package-name>`
4. Review error messages carefully
5. Check firewall/antivirus settings (may block local server)

## macOS-Specific Notes

If you're on macOS and encounter SSL certificate errors:

```bash
# Install certificates
/Applications/Python\ 3.9/Install\ Certificates.command
```

## Windows-Specific Notes

If you're on Windows and encounter path issues:

- Use `python` instead of `python3`
- Use `pip` instead of `pip3`
- Run Command Prompt as Administrator if needed

---

**Installation Complete!**

You're ready to use the SIAMA Stakeholder Analysis Tool with full subgrouping and k-means clustering capabilities.

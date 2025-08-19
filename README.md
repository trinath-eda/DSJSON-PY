## 📄 README.md

### Project: dsjson

A lightweight Python package to convert clinical tabular datasets (e.g., SDTM/ADaM) and metadata into **CDISC Dataset-JSON v1.1** format. It supports multiple metadata input formats including CSV, Excel, JSON, and XML (planned).

[![PyPI version](https://badge.fury.io/py/dsjson.svg)](https://pypi.org/project/dsjson/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


### 🔧 Features

* Converts `DataFrame` + column metadata to Dataset-JSON v1.1
* Supports CSV, Excel, JSON for metadata
* Auto-generates `datasetJSONCreationDateTime`
* Enforces required top-level metadata
* Clean and minimal API

### 📦 Installation
```
pip install dsjson
```

### 🚀 Quick Start

```python
from dsjson import load_metadata, to_dataset_json
import pandas as pd

# Load data and metadata
rows = pd.read_csv("examples/vs.csv")
columns = load_metadata("examples/columns_vs.csv", file_type="csv")

# Create Dataset-JSON
ds = to_dataset_json(
    data_df=rows,
    columns_df=columns,
    name="VS",
    label="Vital Signs",
    itemGroupOID="IG.VS",
    originator="My CRO",
    sourceSystem_name="Python",
    sourceSystem_version="3.10",
    fileOID="F.VS.001",
    studyOID="S.1234"
)
```

### 📁 Supported Input Types

* Column Metadata: `.csv`, `.xlsx`, `.json`, (planned: `.xml`)
* Data Table: Any Pandas-compatible format

### ✅ Output Example

```json
{
  "datasetJSONVersion": "1.1",
  "datasetJSONCreationDateTime": "2025-07-19T00:00:00",
  "name": "VS",
  "label": "Vital Signs",
  "itemGroupOID": "IG.VS",
  "columns": [...],
  "rows": [...],
  "records": 100,
  "originator": "My CRO",
  "sourceSystem": {
    "name": "Python",
    "version": "3.10"
  }
}
```
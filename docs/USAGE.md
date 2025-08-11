## 📄 docs/USAGE.md

### 🛠 Main Function: `create_dataset_json_v1_1`

```python
def to_dataset_json(
    data_df: pd.DataFrame,
    columns_df: pd.DataFrame,
    datasetJSONVersion="1.1",
    itemGroupOID: str,
    name: str,
    label: str,
    originator: str = None,
    sourceSystem_name: str = None,
    sourceSystem_version: str = None,
    fileOID: str = None,
    studyOID: str = None,
    metaDataVersionOID: str = None,
    metaDataRef: str = None,
) -> dict:
```

### 🔄 Examples for Each Format

```python
# CSV
load_metadata("columns_vs.csv", file_type="csv")

# Excel
load_metadata("columns_vs.xlsx", file_type="excel")

# JSON
load_metadata("columns_vs.json", file_type="json")
```

### 🔚 Output

A valid Dataset-JSON dictionary you can write to a file using `json.dump()`.
## 📄 docs/IMPLEMENTATION.md

### 🔍 Functionality

**`core.py`** contains the logic to generate a compliant Dataset-JSON v1.1 structure.

### 🧱 Key Components:

* `load_column_metadata_any`: Loads metadata from any supported format
* `create_dataset_json_v1_1`: Creates the final JSON structure from metadata + data

### 🎯 Design Decisions

* `datasetJSONCreationDateTime`: Auto-generated from `datetime.utcnow()`
* `sourceSystem.name` and `sourceSystem.version`: Passed via function parameters
* `columns_df`: must match data\_df columns; raises error if mismatch
* Required top-level fields: `name`, `label`, `itemGroupOID`, `datasetJSONVersion`
* Optional top-level fields: `originator`, `studyOID`, `fileOID`, etc.

## 📄 docs/TESTING.md

### ✅ Testing Strategy

* Framework: `pytest`
* Tests located in: `tests/test_core.py`

### 🧪 How to Run Tests

```bash
pytest
```

### 📄 Sample Test

```python
def test_to_dataset_json():
    import pandas as pd
    from dsjson import load_metadata, to_dataset_json

    df = pd.read_csv("examples/vs.csv")
    columns = load_metadata("examples/columns_vs.csv")

    result = to_dataset_json(
        data_df=df,
        columns_df=columns,
        name="VS",
        label="Vital Signs",
        itemGroupOID="IG.VS",
        sourceSystem_name="pytest",
        sourceSystem_version="1.0"
    )

    assert result["name"] == "VS"
    assert "columns" in result
    assert "rows" in result
```

### 🧪 Planned Tests

* JSON + Excel input formats
* Mismatched column handling
* Missing required field errors

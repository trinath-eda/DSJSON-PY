import pandas as pd
from dsjson import load_metadata, to_dataset_json
import json

# Load data and metadata
df = pd.read_csv(r"H:\py_Package\dataset_json\examples\vs.csv")
columns_df = load_metadata(r"H:\py_Package\dataset_json\examples\columns_vs.csv", file_type="csv")

# Create Dataset-JSON dict
ds_json = to_dataset_json(
    data_df=df,
    columns_df=columns_df,
    name="VS",
    label="Vital Signs",
    itemGroupOID="IG.VS",  # Required field
    originator="My CRO",
    sourceSystem_name="python", 
    sourceSystem_version="3.10",       
    fileOID="F.VS.001",
    studyOID="S.1234"
)

# Save to JSON file
with open(r"output\vs.json", "w", encoding="utf-8") as f:
    json.dump(ds_json, f, indent=2, ensure_ascii=False)


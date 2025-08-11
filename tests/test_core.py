import pandas as pd
from dsjson import load_column_metadata_any, create_dataset_json_v1_1
import os

# Get the directory of the current test file
tests_dir = os.path.dirname(__file__)
# Construct the relative path to the examples directory
examples_dir = os.path.abspath(os.path.join(tests_dir, '..', 'examples'))

def test_create_dataset_json():
    # Use the relative paths to load the files
    df = pd.read_csv(os.path.join(examples_dir, "vs.csv"))
    columns_df = load_column_metadata_any(os.path.join(examples_dir, "columns_vs.csv"))

    result = create_dataset_json_v1_1(
        data_df=df,
        columns_df=columns_df,
        name="VS",
        label="Vital Signs",
        itemGroupOID="IG.VS",
        sourceSystem_name="TestTool",
        sourceSystem_version="1.0"
    )

    assert result["name"] == "VS"
    assert "rows" in result
    assert "columns" in result
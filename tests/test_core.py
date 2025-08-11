import pandas as pd
from dsjson import load_metadata, to_dataset_json
import os

# Get the directory of the current test file
tests_dir = os.path.dirname(__file__)
# Construct the relative path to the examples directory
examples_dir = os.path.abspath(os.path.join(tests_dir, '..', 'examples'))

def test_create_dataset_json():
    # Use the relative paths to load the files
    df = pd.read_csv(os.path.join(examples_dir, "vs.csv"))
    columns_df = load_metadata(os.path.join(examples_dir, "columns_vs.csv"))

    result = to_dataset_json(
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
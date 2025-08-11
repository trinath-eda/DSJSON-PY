def test_create_dataset_json():
    import pandas as pd
    from dsjson import load_column_metadata_any, create_dataset_json_v1_1

    df = pd.read_csv(r"H:\py_Package\dataset_json\examples\vs.csv")
    columns_df = load_column_metadata_any(r"H:\py_Package\dataset_json\examples\columns_vs.csv")

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

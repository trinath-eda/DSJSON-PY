def test_to_dataset_json():
    import pandas as pd
    from dsjson import load_metadata, to_dataset_json

    df = pd.read_csv(r"H:\py_Package\dataset_json\examples\vs.csv")
    columns_df = load_metadata(r"H:\py_Package\dataset_json\examples\columns_vs.csv")

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

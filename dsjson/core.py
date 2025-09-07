import pandas as pd
import numpy as np
from datetime import datetime
from collections import OrderedDict
from typing import Optional, Dict, Any, Union
from pathlib import Path


def load_metadata(
    source: Union[pd.DataFrame, str, Path], 
    file_type: str = "csv"
) -> pd.DataFrame:
    """
    Load column metadata from different formats (csv, excel, json, xml, DataFrame).
    """
    if isinstance(source, pd.DataFrame):
        return source
    if file_type == "csv":
        return pd.read_csv(source)
    elif file_type == "excel":
        return pd.read_excel(source)
    elif file_type == "json":
        return pd.read_json(source)
    elif file_type == "xml":
        return pd.read_xml(source)
    else:
        raise ValueError("Unsupported file_type. Use 'csv', 'excel', 'json', 'xml', or a DataFrame.")


def to_dataset_json(
    data_df: pd.DataFrame,
    columns_df: pd.DataFrame,
    datasetJSONVersion: str = "1.1",
    name: Optional[str] = None,
    label: str = None,
    itemGroupOID: str = None,  # Required
    # Compound top-level fields
    sourceSystem_name: str = None,
    sourceSystem_version: str = None,
    # Optional top-level fields
    fileOID: str = None,
    dbLastModifiedDateTime: str = None,
    originator: str = None,
    studyOID: str = None,
    metaDataVersionOID: str = None,
    metaDataRef: str = None,
    **kwargs
) -> dict[str, Any]:
    """
    Create a CDISC-compliant Dataset-JSON v1.1 structure with strict key ordering.
    """
        # Add input validation
    if not isinstance(data_df, pd.DataFrame):
        raise TypeError("data_df must be a pandas DataFrame")
    if not isinstance(columns_df, pd.DataFrame):
        raise TypeError("columns_df must be a pandas DataFrame")
    if columns_df.empty:
        raise ValueError("columns_df cannot be empty")

    # Auto-generate creation timestamp
    datasetJSONCreationDateTime = datetime.now().isoformat()

    # Validate required fields
    required_fields = {
        "datasetJSONVersion": datasetJSONVersion,
        "datasetJSONCreationDateTime": datasetJSONCreationDateTime,
        "name": name,
        "label": label,
        "itemGroupOID": itemGroupOID
    }
    for key, val in required_fields.items():
        if val is None:
            raise ValueError(f"{key} is required")

    # Validate metadata/data alignment
    column_names = columns_df["name"].tolist()
    missing = [col for col in column_names if col not in data_df.columns]
    if missing:
        raise ValueError(f"Missing columns in row data: {missing}")
    
    # Make a copy and handle missing values
    data_df = data_df[column_names].copy()
    # Replace NaN and None with None (which will be converted to null in JSON)
    data_df = data_df.replace({np.nan: None})
    data_df = data_df.where(pd.notna(data_df), None)

    # Assemble compound sourceSystem
    sourceSystem = None
    if sourceSystem_name or sourceSystem_version:
        if not (sourceSystem_name and sourceSystem_version):
            raise ValueError("Both sourceSystem_name and sourceSystem_version must be provided.")
        sourceSystem = {
            "name": sourceSystem_name,
            "version": sourceSystem_version
        }

    # Create final structure with enforced key order
    dataset_json = OrderedDict()
    dataset_json["datasetJSONCreationDateTime"] = datasetJSONCreationDateTime
    dataset_json["datasetJSONVersion"] = datasetJSONVersion
    if fileOID:
        dataset_json["fileOID"] = fileOID
    if dbLastModifiedDateTime:
        dataset_json["dbLastModifiedDateTime"] = dbLastModifiedDateTime
    if originator:
        dataset_json["originator"] = originator
    if sourceSystem:
        dataset_json["sourceSystem"] = sourceSystem
    if studyOID:
        dataset_json["studyOID"] = studyOID
    if metaDataVersionOID:
        dataset_json["metaDataVersionOID"] = metaDataVersionOID
    if metaDataRef:
        dataset_json["metaDataRef"] = metaDataRef

    dataset_json["itemGroupOID"] = itemGroupOID
    dataset_json["records"] = len(data_df)
    dataset_json["name"] = name
    dataset_json["label"] = label
    dataset_json["columns"] = columns_df.to_dict(orient="records")
# Use this for large datasets:
    dataset_json["rows"] = [
        [None if pd.isna(val) else val for val in row] 
        for row in data_df.values
    ]

    # Add any additional top-level metadata if provided via kwargs
    dataset_json.update(kwargs)

    return dataset_json

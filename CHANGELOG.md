# Changelog

## [1.1] - 2025-09-07
### Enhancements:
- Replaced NaN values with null in the final JSON output for better JSON compliance.
- Added validation for columns_df to ensure they are non-empty and of the correct type.
- Optimized row processing for large datasets by using list comprehensions.
- Added specific type hints for better code maintainability and clarity.

## [1.0] - 2025-08-20
### Added
- First stable release published to PyPI.

## [0.1.1] - 2025-08-11
### Updated
- Renamed `load_column_metadata_any` to `load_metadata`
- Renamed `create_dataset_json_v1_1` to `to_dataset_json`

## [0.1.0] - 2025-07-19
### Added
- Initial release
- Core function: `create_dataset_json_v1_1`
- Metadata loader: `load_column_metadata_any`
- Support for metadata in CSV, Excel, JSON
- Auto datetime field generation
- Single example and working test

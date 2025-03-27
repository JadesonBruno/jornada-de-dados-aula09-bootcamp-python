# importing python standard libraries
from pathlib import Path
from typing import List

# importing third party libraries
import pandas as pd

# importing local modules
from etl import (
    calculate_kpi_of_total_sales,
    extract_and_consolidate_json_files,
    load_data,
)


def main():
    # defining path
    files_path: Path = Path("data")

    # defining df_total
    df_total: pd.DataFrame = extract_and_consolidate_json_files(path=files_path)

    # df_total_with_total_sales
    df_total_with_total_sales: pd.DataFrame = calculate_kpi_of_total_sales(dataframe=df_total)

    # defining format to exit
    files_type_to_export: List[str] = ["csv", "parquet"]
    # exporting data
    load_data(sales_dataframe=df_total_with_total_sales, exit_format=files_type_to_export)


# call main function in python
if __name__ == "__main__":
    main()

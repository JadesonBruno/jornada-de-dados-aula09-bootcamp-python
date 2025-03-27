# import python standard libraries
import glob
import os
from pathlib import Path
from typing import List

# importing third party libraries
import pandas as pd

# Importando módulos
from utils_log import log_decorator


@log_decorator
def extract_and_consolidate_json_files(path: Path) -> pd.DataFrame:
    """
    Function that extracts data from multiple json files and consolidates
    them into a pandas dataframe.
    """
    json_files: List[Path] = glob.glob(os.path.join(path, "*.json"))

    dataframes_list: List[pd.DataFrame] = [pd.read_json(json_file) for json_file in json_files]
    df_total: pd.DataFrame = pd.concat(dataframes_list, ignore_index=True)

    return df_total


@log_decorator
def calculate_kpi_of_total_sales(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Function that creates a new calculated column for total sales.
    """
    new_dataframe: pd.DataFrame = dataframe.copy()
    new_dataframe["total_sales"] = new_dataframe["Quantidade"] * new_dataframe["Venda"]

    return new_dataframe


@log_decorator
def load_data(sales_dataframe: pd.DataFrame, exit_format: List[str]) -> None:
    """
    Function that exports data to a csv file or parquet file.
    """
    if "csv" in exit_format:
        sales_dataframe.to_csv(path_or_buf="output/data.csv", index=False)
        print("Exporting to csv.")

    if "parquet" in exit_format:
        sales_dataframe.to_parquet(path="output/data.parquet", index=False)
        print("Exporting to parquet.")


@log_decorator
def pipeline_to_calculate_consolidated_sales_kpi(files_path: Path, files_type_to_export: List) -> None:
    """
    Consolidates the entire pipeline to facilitate user calls.
    """
    # defining df_total
    df_total: pd.DataFrame = extract_and_consolidate_json_files(path=files_path)

    # df_total_with_total_sales
    df_total_with_total_sales: pd.DataFrame = calculate_kpi_of_total_sales(dataframe=df_total)

    # exporting data
    load_data(sales_dataframe=df_total_with_total_sales, exit_format=files_type_to_export)

# OOP Data Processing Lab (Commit 3)

## Lab Overview
This project refactors procedural CSV data-processing code into an Object-Oriented Programming (OOP) design in Python. It encapsulates CSV file loading into a `DataLoader` class and models tabular datasets as `Table` objects that support filtering, aggregation, and column selection.

## Project Structure
data_processing_lab/
│
├── README.md              # Project documentation
├── Cities.csv             # The dataset containing city coordinates and temperatures
└── data_processing.py     # The OOP analysis code and test script


## Design Overview

### `DataLoader`
Handles reading CSV files from disk and converting them into a list of dictionaries.
* **Attributes:**
  * `base_path` (`Path`): Directory path where dataset files are stored (defaults to the directory containing `data_processing.py`).
* **Key Methods:**
  * `load_csv(filename)`: Reads the specified CSV file using `csv.DictReader` and returns a `list` of `dict` rows.

### `Table`
Represents a dataset table and provides methods to query and summarize the data.
* **Attributes:**
  * `table_name` (`str`): Identifier name for the table (e.g., `'cities'`).
  * `table` (`list[dict]`): List of row dictionaries representing the table records.
* **Key Methods:**
  * `filter(condition)`: Takes a predicate function (e.g., a `lambda`) and returns a new `Table` containing only the rows that satisfy the condition.
  * `aggregate(aggregation_function, aggregation_key)`: Extracts all values under `aggregation_key` (converting numeric strings to `float` when possible) and applies `aggregation_function` (such as average, `max`, or `len(set(...))`).
  * `select(attributes_list)`: Returns a new `Table` containing only the columns specified in `attributes_list`.
  * `__str__()`: Returns a formatted string representation of the table name and its rows.

## How to Test and Run
1. Ensure `data_processing.py` and `Cities.csv` are in the same directory.
2. Run the script from your terminal:
   ```bash
   python data_processing.py
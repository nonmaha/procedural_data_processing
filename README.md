# OOP Data Processing Lab (Commit 4)

## Lab Overview
This project refactors procedural CSV data-processing code into an Object-Oriented Programming (OOP) design in Python. It encapsulates CSV loading (`DataLoader`), relational table operations (`Table`), and multi-table storage (`DB`), supporting filtering, aggregation, column selection, and inner joins across multiple datasets (`Cities.csv` and `Countries.csv`).

## Project Structure
```text
procedural_data_processing/
│
├── README.md              # Project documentation
├── Cities.csv             # Dataset containing city coordinates and temperatures
├── Countries.csv          # Dataset containing country populations, EU status, and coastlines
└── data_processing.py     # Main OOP implementation and test script
```


## Design Overview

### `DataLoader`
Handles reading CSV files from disk and converting them into a list of dictionaries.
* **Attributes:**
  * `base_path` (`Path`): Directory path where dataset files are stored (defaults to the directory containing `data_processing.py`).
* **Key Methods:**
  * `load_csv(filename)`: Reads the specified CSV file using `csv.DictReader` and returns a `list` of `dict` rows.

### `DB`
Acts as an in-memory database container that stores and retrieves multiple `Table` objects.
* **Attributes:**
  * `database` (`list[Table]`): List holding inserted `Table` instances.
* **Key Methods:**
  * `insert(table)`: Appends a `Table` object to `self.database`.
  * `search(table_name)`: Searches `self.database` by `table_name` and returns the matching `Table` object (or `None` if not found).

### `Table`
Represents a dataset table and provides relational query and summary operations.
* **Attributes:**
  * `table_name` (`str`): Identifier name for the table (e.g., `'cities'`, `'countries'`).
  * `table` (`list[dict]`): List of row dictionaries representing the table records.
* **Key Methods:**
  * `join(other_table, common_key)`: Performs an inner join between `self` and `other_table` on `common_key`, merging matching rows into a new `Table` named `<table_name>_joins_<other_table_name>`.
  * `filter(condition)`: Takes a predicate function (e.g., a `lambda`) and returns a new `Table` containing only rows that satisfy the condition.
  * `aggregate(aggregation_function, aggregation_key)`: Extracts values under `aggregation_key` (converting numeric strings to `float` when possible) and applies `aggregation_function` (such as average, `min`, `max`, or `len(set(...))`).
  * `select(attributes_list)`: Returns a new `Table` containing only the columns specified in `attributes_list`.
  * `__str__()`: Returns a formatted string representation of the table name and its rows.

## How to Test and Run
1. Ensure `data_processing.py`, `Cities.csv`, and `Countries.csv` are in the same directory.
2. Run the script from your terminal:
   ```bash
   python data_processing.py
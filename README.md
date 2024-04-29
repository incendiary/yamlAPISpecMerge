# YAML API Spec Merger

This Python script parses all YAML files in a given directory and generates a summary of the API paths and HTTP methods used in those files. It supports all standard HTTP methods (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, TRACE) and provides a count for each method used across all files.

## Prerequisites

- Python 3.x
- `pyyaml` library

You can install the required dependencies by running:

`pip install -r requirements.txt`

## Usage

To run the script, use the following command:

`python yamlAPISpecMerge.py <directory>`

Replace `<directory>` with the path to the directory containing your YAML API specification files.

## Example Output

/example/api/resource/{id}
- PUT: 1
- GET: 1

/example/api/another-resource/{id}/update
- PUT: 1

Total:
PUT: 2
GET: 1

The script will print the summary of paths and methods, as well as the total counts for each method.

## How it Works

1. The script imports the necessary modules and defines a list of standard HTTP methods.
2. The `parse_yaml_files` function takes a directory path as an argument.
3. Inside the function, two `defaultdict` objects are initialized: `path_summary` and `method_counts`. The `path_summary` dictionary will store the method counts for each path, and the `method_counts` dictionary will store the total count for each method.
4. The code iterates over all files in the directory with a `.yaml` extension.
5. For each YAML file, it uses `pyyaml.safe_load_all` to load all documents in the file.
6. For each document, it checks if the 'paths' key exists. If it does, it iterates over the paths and methods.
7. For each method, it converts it to uppercase and checks if it's in the `HTTP_METHODS` list.
8. If the method is valid, it increments the count in `path_summary` for that path and method, and also increments the total count in `method_counts`.
9. After processing all files, the code prints the summary by iterating over `path_summary` and `HTTP_METHODS`.
10. Finally, it prints the total counts for each method.


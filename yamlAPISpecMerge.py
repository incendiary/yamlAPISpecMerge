import os
import sys
import yaml
from collections import defaultdict

HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS', 'TRACE']


def parse_yaml_files(directory):
    path_summary = defaultdict(lambda: defaultdict(int))
    method_counts = defaultdict(int)

    for filename in os.listdir(directory):
        if filename.endswith('.yaml'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = yaml.safe_load_all(file)
                for doc in data:
                    if doc and 'paths' in doc:
                        for path, path_info in doc['paths'].items():
                            for method in path_info.keys():
                                method = method.upper()
                                if method in HTTP_METHODS:
                                    path_summary[path][method] += 1
                                    method_counts[method] += 1

    for path, method_count in path_summary.items():
        print(path)
        for method in HTTP_METHODS:
            count = method_count[method]
            if count > 0:
                print(f"- {method}: {count}")
        print()

    print("Total:")
    for method in HTTP_METHODS:
        count = method_counts[method]
        if count > 0:
            print(f"{method}: {count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    parse_yaml_files(directory)

import sys


def check_arg(bash_args: list):
    if len(bash_args) == 0:
        print(f"no keys were defined as arguments for script: {bash_args}\nprogram will be terminated")
        sys.exit(1)

def check_arg_and_json(json_data: dict, keys: list):
    for key in keys:
        for row in json_data:
            if not key in row.keys():
                print(f"key: {key} is not present in json to parse:\n {json_data}\nprogram will be terminated")
                sys.exit(1)
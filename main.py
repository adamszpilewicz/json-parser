import argparse
from inputs.checks import check_arg, check_arg_and_json
import json
import sys

from encoders.jsons import json_restructure 


parser = argparse.ArgumentParser(
    prog="encoding json", description="parse json by defining keys to nest"
)

parser.add_argument(
    "input",
    action="store",
    nargs="*",
    help="list of arguments defining keys that are present in json; they must exactly match keys from json to be parsed"
)

args = parser.parse_args()


def main(): 
    data = json.load(sys.stdin)
    check_arg(args.input)
    check_arg_and_json(data, args.input)
    storage = []
    for data in data:
        storage.append(json_restructure(args.input, data))
    print(storage)


if __name__ == "__main__":
    main()
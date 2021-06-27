import argparse
from api.api import app

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8080",debug=True)


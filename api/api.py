from flask import Flask, request, jsonify
from encoders.jsons import json_restructure
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "adam": generate_password_hash("secretpass"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/parser', methods=['POST'])
@auth.login_required
def parser():
    storage = []
    content = request.json
    args = []
    for i in request.args.values():
        args.append(i)
    for data in content:
        flag, arg = check_input(args, data.keys())
        if not flag:
            return f'bad request! \nargs passed in request: {arg} \nnot found in json: {list(data.keys())}', 400
        storage.append(json_restructure(args, data))
    return jsonify(storage)

def check_input(args_passed: str, keys_json: str) -> bool:
    for arg in args_passed:
        if arg not in keys_json:
            return False, arg
    return True, arg

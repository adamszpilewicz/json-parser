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
        storage.append(json_restructure(args, data))
    return jsonify(storage)


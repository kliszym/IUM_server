from db_connection import DbConnection

from google.oauth2 import id_token
from google.auth.transport import requests as g_requests

from flask import request
from flask import Response
import json

import Login

from flask import Flask

from sessions import Sessions

app = Flask(__name__)

app.secret_key = "some random characters!"


@app.route('/info', methods=['POST'])
def info():
    print(request.get_json())
    if Sessions.verify_id(request.get_json()['id']):
        result = DbConnection.get_content()
        result = json.dumps(result)
        return Response(result, content_type='application/json')
    return {'response': 'unauthorized'}, 401


@app.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    is_success, master_role, user_id = Login.login(credentials)
    print(bool(master_role))
    if is_success:
        return {'role': bool(master_role), 'id': user_id}, 201
    else:
        return {'response': 'fail'}, 401


@app.route('/token', methods=['POST'])
def token():
    g_token = request.get_json()['token']
    print(g_token)
    try:
        idinfo = id_token.verify_oauth2_token(g_token, g_requests.Request(), '293750822743-21b25nnboijc6f2bn8p73qpkt77ihajq.apps.googleusercontent.com')
        print(idinfo)
        email = idinfo['email']
        user_id = Sessions.get_id(email)
        return {'username': email, 'role': False, 'id': user_id}, 201
    except ValueError:
        return {'response': 'unauthorized'}, 401


@app.route('/update', methods=['POST'])
def update():
    print(request.get_json())
    if Sessions.verify_id(request.get_json()['id']):
        DbConnection.update_content(request.get_json()["products"])
        return {'response': 'success'}, 200
    return {'response': 'unauthorized'}, 401


@app.route('/create', methods=['POST'])
def create():
    print(request.get_json())
    if Sessions.verify_id(request.get_json()['id']):
        result = DbConnection.create_product(request.get_json()["products"])
        return {'response': 'success', 'result': result}, 200
    return {'response': 'unauthorized'}, 401


@app.route('/remove', methods=['POST'])
def remove():
    print(request.get_json())
    if Sessions.verify_id(request.get_json()['id']) and Sessions.is_master(request.get_json()['id']):
        DbConnection.remove_product(request.get_json()["products"])
        return {'response': 'success'}, 200
    return {'response': 'unauthorized'}, 401


@app.route('/increase', methods=['POST'])
def increase():
    print(request.get_json())
    if Sessions.verify_id(request.get_json()['id']):
        DbConnection.increase(request.get_json()["products"])
        return {'response': 'success'}, 200
    return {'response': 'unauthorized'}, 401


@app.route('/decrease', methods=['POST'])
def decrease():
    print(request.get_json())
    if Sessions.verify_id(request.get_json()['id']):
        DbConnection.decrease(request.get_json()["products"])
        return {'response': 'success'}, 200
    return {'response': 'unauthorized'}, 401


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, threaded=False)

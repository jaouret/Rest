from flask import Flask, jsonify, request
import db01_crud
from db01 import create_tables

app = Flask(__name__)

# contexts
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/rest_testSCD30', methods=["GET"])
def get_dataSCD30():
    dataSCD30 = db01_crud.get_dataSCD30()
    return jsonify(dataSCD30)

@app.route("/rest_testSCD30", methods=["POST"])
def insert_dataSCD30():
    dataSCD30_details = request.get_json()
    co2 = dataSCD30_details["co2"]
    temp = dataSCD30_details["temp"]
    hum = dataSCD30_details["hum"]
    result = db01_crud.insert_dataSCD30(co2, temp, hum)
    return jsonify(result)


@app.route("/rest_testSCD30", methods=["PUT"])
def update_dataSCD30():
    dataSCD30_details = request.get_json()
    id = dataSCD30_details["id"]
    co2 = dataSCD30_details["co2"]
    temp = dataSCD30_details["temp"]
    hum = dataSCD30_details["hum"]
    result = db01_crud.update_dataSCD30(id, co2, temp, hum)
    return jsonify(result)

@app.route("/rest_testSCD30/<id>", methods=["DELETE"])
def delete_dataSCD30(id):
    result = db01_crud.delete_dataSCD30(id)
    return jsonify(result)


@app.route("/rest_testSCD30/<id>", methods=["GET"])
def get_dataSCD30_by_id(id):
    dataSCD30 = db01_crud.get_by_id(id)
    return jsonify(dataSCD30)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='127.0.0.1', port=8000, debug=True)


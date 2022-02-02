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

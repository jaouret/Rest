from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

#Create an instance of Flask
app = Flask(__name__)
#Create an instance of MySQL
mysql = MySQL()
#Create an instance of Flask RESTful API
api = Api(app)
#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'javier'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Clay2836'
app.config['MYSQL_DATABASE_DB'] = 'data_iot1'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
#app.config['MYSQL_DATABASE_PORT'] = '5522'
#Initialize the MySQL extension
mysql.init_app(app)
#Get All Users, or Create a new user
class Id(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from data1""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            #_id = request.form['id']
            _co2 = request.form['co2']
            _temp = request.form['temp']
            _hum = request.form['hum']
            insert_id_cmd = """INSERT INTO data1(co2, temp, hum) 
                                VALUES(%s, %s, %s)"""
            cursor.execute(insert_id_cmd, (_co2, _temp, _hum))
            conn.commit()
            response = jsonify(message='Datos ingresados correctamente.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add data.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            

#API resource routes
api.add_resource(Id, '/id', endpoint='id')

if __name__ == "__main__":
    app.run(debug=True)
    
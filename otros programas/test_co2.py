from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import sqlite3
from sqlite3 import Error

#db_connect = create_engine('sqlite:///co2.db')
#conn = sqlite3.connect('co2.db')
app = Flask(__name__)
api = Api(app)
#cur = conn.cursor()
#cur.execute("SELECT * FROM data1")
#rows = cur.fetchall()
#for row in rows:
#    print(row)

class Id(Resource):
    def get(self):
        conn = sqlite3.connect('../co2.db') #conn = db_connect.connect() # connect to database
        cur = conn.cursor()
        query = conn.execute("select * from data1") # This line performs query and returns json result
        dato=cur.fetchall()
        for i in dato:
            print (i[0]) # Fetches first column that is ID
        result = {'ID': i[0]} # Fetches first column that is ID
        return jsonify(result)

class CO2(Resource):
    def get(self):
        #conn = db_connect.connect()
        conn = sqlite3.connect('../co2.db')
        cur = conn.cursor()
        query = conn.execute("select id, co2, temp, hum from data1")
        result = {'data': [dict(zip(tuple (keys()) ,i)) for i in cur.fetchall()]}
        return jsonify(result)

class Dato(Resource):
    def get(self, id):
        #conn = db_connect.connect()
        query = conn.execute("select * from data1 where Id =%d "  %int(id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Id, '/id') # Route_1
api.add_resource(CO2, '/co2') # Route_2
api.add_resource(Dato, '/Dato/<id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')

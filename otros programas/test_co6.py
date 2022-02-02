from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
#Create an instance of Flask RESTful API
api = Api(app)

app.config['MYSQL_USER'] = 'javier'
app.config['MYSQL_PASSWORD'] = 'Clay2836'
app.config['MYSQL_DB'] = 'data_iot1'
#app.config['MYSQL_PORT'] = '5522'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

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


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''select * from data1''')
    rv = cur.fetchall()
    return str(rv)

api.add_resource(Id, '/id', endpoint='id')


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
from db01 import get_db

def insert_dataSCD30(co2, temp, hum):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO tabla_REST_testSCD30(co2, temp, hum) VALUES (?, ?, ?)"
    cursor.execute(statement, [co2, temp, hum])
    db.commit()
    return True

def update_dataSCD30(co2, temp, hum):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE tabla_REST_testSCD30 SET co2 = ?, temp = ?, hum = ? WHERE id = ?"
    cursor.execute(statement, [co2, temp, hum, id])
    db.commit()
    return True

def delete_dataSCD30(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM tabla_REST_testSCD30 WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, co2, temp, hum, fecha FROM tabla_REST_testSCD30 WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_dataSCD30():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, co2, temp, hum, fecha FROM tabla_REST_testSCD30"
    cursor.execute(query)
    return cursor.fetchall()
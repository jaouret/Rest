import sqlite3
DATABASE_NAME = "REST_test.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS tabla_REST_testSCD30(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                co2 REAL,
				temp REAL,
				hum REAL,
				fecha datetime default current_timestamp
            )
            """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
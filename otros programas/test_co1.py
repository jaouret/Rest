import sqlite3
conn = sqlite3.connect('../co2.db')

cur = conn.cursor()

cur.execute('SELECT * FROM data1 ORDER BY id')

datos = cur.fetchall()

for data in datos:

    print(f'{data[0]} {data[1]}')
    
id = '1'
cur.execute('SELECT * FROM data1 WHERE id = \'{}\''.format(id))
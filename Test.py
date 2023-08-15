import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='12345', host='localhost')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Test LIMIT 10')
records = cursor.fetchall()
print(records)
import psycopg2
import sqlalchemy
conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='12345', host='localhost', port="5432")
cursor = conn.cursor()
cursor.execute('SELECT * FROM public."Test"')
rows = cursor.fetchall()

print(rows)
import json
import psycopg2
from psycopg2.extras import Json
from psycopg2.extensions import AsIs

def json_test():
    # подключение к бд
    con = psycopg2.connect(user="postgres",
                            password="12345",
                            host="localhost",
                            port="5432")
    cur = con.cursor()
    # берем некоторые поля из бд
    cur.execute('Select id, cont_number, cont_type from test')
    query = cur.fetchall()
    # цикл добавления данных в бд, одна колонка имеет тип json
    for cont in query:
        print(cont)
        cur.execute('INSERT INTO cont (id, cont_data) VALUES (%s, %s);', (cont[0], json.dumps({"1": cont[1], "2": cont[2]})))
        con.commit
    # посылаем запрос в нашу заполненную таблицу
    cur.execute('select * from cont')
    query = cur.fetchall()
    # проверка обращения к объекту
    for row in query:
        print(row[1]["1"])
    con.close
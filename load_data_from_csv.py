import csv
import psycopg2

def load_data():
    con = psycopg2.connect(user="postgres",
                           password="12345",
                           host="localhost",
                           port="5432")
    cur = con.cursor()
    with open('test.csv', 'r', encoding='utf-8') as fin:
        dr = csv.DictReader(fin, delimiter = ';')
        to_db = [(Column['ID'], 
                Column['ВТТ'],
                Column['Дата прибытия по ж/д'],
                Column['HBL'],
                Column['Дата релиза HBL'],
                Column['Таможенный пост'],
                Column['Дата проверки'],
                Column['Дата создания заказа'],
                Column['Дата получения'],
                Column['Клиент'],
                Column['Поставщик'],
                Column['Номер инвойса'],
                Column['Брокер'],
                Column['Получатель'],
                Column['Экспедитор'],
                Column['Склад'],
                Column['Номер контейнера'],
                Column['Тип конт.'],
                Column['Усл. поставки'],
                Column['Место отправки'],
                Column['Страна отправки'],
                Column['Место доставки'],
                Column['Страна доставки'],
                Column['Линия'],
                Column['Агент'],
                Column['Товар'],
                Column['Номер заказа'],
                Column['Кол-во мест'],
                Column['Вес брутто'],
                Column['Объем'],
                Column['Стоимость'],
                Column['Особые условия погрузки'],
                Column['Дата готовн.'],
                Column['Дата загрузки'],
                Column['Packing'],
                Column['Дата выхода в море'],
                Column['Коносамент'],
                Column['Подготовка коммерческих документов'],
                Column['Telex'],
                Column['Примечание'],
                Column['Дата отправки док-тов'],
                Column['Дата прибытия'],
                Column['Порт'],
                Column['Дата получ. док-тов'],
                Column['Дата подачи декларации'],
                Column['Дата выпуска декларации'],
                Column['Номер декларации'],
                Column['Дата отправки по ж/д'],
                Column['Дата выгрузки']) for Column in dr]
    cur.executemany("INSERT INTO test (id, btt, date_arr_jd, hbl, date_real_hbl, customs_post, date_check, date_create_order, date_get_order, customer, provider, \
                    invoice_number, broker, recipient, forwarder, store, cont_number, cont_type, del_cond, place_dispatch, country_dispatch, place_delivery,\
                    country_delivery, line_w, agent, goods, order_number, number_places, weight,volume,price,spec_load_cond,date_ready,date_load,date_pack,date_enter_sea,\
                    consignment_number,date_prepare_doc,date_telex,note,date_send_docs,date_arr,port_name,date_get_doc, date_send_decl,date_iss_decl, \
                    decl_number,date_send_jd,date_unload)\
    VALUES (%s, %s, NULLIF(%s, '')::date, %s, NULLIF(%s, '')::date, %s, NULLIF(%s, '')::date, NULLIF(%s, '')::date, NULLIF(%s, '')::date, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
            %s, %s, %s, %s, %s, %s, %s, %s, %s, NULLIF(%s, '')::int, NULLIF(%s, '')::float, NULLIF(%s, '')::float, NULLIF(%s, '')::float, %s, NULLIF(%s, '')::date, NULLIF(%s, '')::date, NULLIF(%s, '')::date, NULLIF(%s, '')::date, %s, \
            NULLIF(%s, '')::date, NULLIF(%s, '')::date, %s, NULLIF(%s, '')::date, NULLIF(%s, '')::date, %s, NULLIF(%s, '')::date, NULLIF(%s, '')::date, \
            NULLIF(%s, '')::date, %s, NULLIF(%s, '')::date, NULLIF(%s, '')::date);", to_db)
    con.commit()
    con.close()
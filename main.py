import os
from models.database import DATABASE_NAME
import create_database as db_creator
from load_data_from_csv import load_data
from work_with_json import json_test
# запускаем этот файл
if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        # функция создания бд
        db_creator.create_database()
        # функция загрузки данных из csv
        load_data()
        json_test()
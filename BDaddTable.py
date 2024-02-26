import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user='postgres',
        password='128POPg',
        host='127.0.0.1',
        port='5432' # !!! Если нужна уже созданная таблица, следующим пунктом нужно указать 'database="DB_name"'
    ) 

    cursor = connection.cursor() # Подключаем возможность выполнения операций с БД
    
    create_table_query = '''CREATE TABLE employees
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            POST            TEXT    NOT NULL,
                            SALARY          REAL    NOT NULL); '''
    
    cursor.execute(create_table_query) # Создание новой таблицы
    connection.commit()

    print('Таблица была успешно добавлена') # Проверка добавления таблицы в БД

except (Exception, Error) as error:
    print('Ошибка при работе с базой данных', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с БД закрыто')
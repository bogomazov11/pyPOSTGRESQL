import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user='postgres',
        password='128POPg',
        host='127.0.0.1',
        port='5432'
    ) 

    cursor = connection.cursor() # Подключаем возможность выполнения операций с БД
    
    insert_query = ''' INSERT INTO employees (ID, NAME, POST, SALARY) 
                    VALUES (1, 'Dmitriy', 'Front-End', 125000) ''' 
    cursor.execute(insert_query) # Первый способ добавления данных
    connection.commit() # Сохранение изменений в БД

    insert_query = ''' INSERT INTO employees (ID, NAME, POST, SALARY)
                    VALUES (%s, %s, %s, %s) '''
    employee_tuple = (2, 'Anna', 'FullstackDev', 200000) 
    cursor.execute(insert_query, employee_tuple) # Второй способ добавления данных
    connection.commit() # Сохранение изменений в БД

    print('Элементы были успешно добавлены в таблицу') # Проверка добавления данных в таблицу


except (Exception, Error) as error:
    print('Ошибка при работе с базой данных', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с БД закрыто')
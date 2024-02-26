import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user='postgres',
        password='128POPg',
        host='127.0.0.1',
        port='5432'
    ) 

    cursor = connection.cursor() 
    
    delete_query = '''DELETE FROM employees WHERE id = 2''' 

    cursor.execute(delete_query) # Фиксируем обновление в БД
    connection.commit() # Сохраняем изменения

    print('Запись удалена') 

    cursor.execute('SELECT * FROM employees')
    print('Результат:', cursor.fetchall()) 

except (Exception, Error) as error:
    print('Ошибка при работе с базой данных', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с БД закрыто')
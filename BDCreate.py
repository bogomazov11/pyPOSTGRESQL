import psycopg2 # Подключение модуля для работы с PostgreSQL
from psycopg2 import Error # С помощью класса Error можно будет подробно разобрать ошибку
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(
        user='postgres',
        password='128POPg',
        host='127.0.0.1',
        port='5432',
    ) 
    ''' 
    Cначала скачиваем postgresql, регистрируемся,
    после вводим данные, введеные при регистрации
    для успешного выполнения операций
    '''
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor() # Подключаем возможность выполнения операций с БД
    
    sql_create_database = 'CREATE DATABASE postgresPLUSpy_db'
    cursor.execute(sql_create_database) # С помощью execute выполняется любая операция или запрос к БД

    print('Инф. о соединении PostgreSQL:')
    print(connection.get_dsn_parameters(), '\n')
    

except (Exception, Error) as error:
    print('Ошибка при работе с базой данных', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с БД закрыто')

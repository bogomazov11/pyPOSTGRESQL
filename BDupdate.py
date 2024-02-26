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
    
    update_query = '''UPDATE employees SET SALARY = 255000 WHERE id = 2''' # Здесь указываем 
    # значение, которое хотим определить (нужную строку определям по id сотрудника) 

    cursor.execute(update_query) # Фиксируем обновление в БД
    connection.commit() # Сохраняем изменения

    print('Запись обновлена') # Удостоверимся в этом
    # Если строка вывелась, значит операция прошла успешно
    
    cursor.execute('SELECT * FROM employees')
    print('Результат:', cursor.fetchall()) # Вывод всей таблицы

except (Exception, Error) as error:
    print('Ошибка при работе с базой данных', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с БД закрыто')
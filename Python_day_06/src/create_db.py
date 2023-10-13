import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Имя текущей базы данных
CURRENT_DB_NAME = 'postgres'
# Имя пользователя
USER = 'marsel'
# Имя новой базы данных
NEW_DB_NAME = 'ex_03'

# Устанавливаем соединение с postgres
connection = psycopg2.connect(dbname=CURRENT_DB_NAME, user=USER)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
# Создаем базу данных
sql_create_database = cursor.execute(f'create database {NEW_DB_NAME}')
# Закрываем соединение
cursor.close()
connection.close()

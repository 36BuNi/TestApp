import os

try:
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    port = os.environ['POSTGRES_PORT']
    database = os.environ['POSTGRES_DB']
    print(f'Настройки доступа к БД взяты из переменного окружения')
except Exception as e:
    user = 'postgres'
    password = 'postgres'
    host = 'localhost'
    port = 5000
    database = 'postgres'
    print(f'{e}.\n'
          f'Настройки доступа к БД взяты по умолчанию')

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

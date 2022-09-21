from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app import config


app = Flask(__name__)
api = Api(app)

# Конфигурация приложения для работы с Бд и документацией.
app.config['APISPEC_TITLE'] = 'Трекер задач'
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['APISPEC_SWAGGER_UI_URL'] = "/"

# Отключает warning SQLALCHEMY.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создание объекта  sqlalchemy базы данных .
db = SQLAlchemy(app)

# Необходимо для создания миграций.
from app import models, routes

# Создание объекта миграции.
migrate = Migrate(app, db)

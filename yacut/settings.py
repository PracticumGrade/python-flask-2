import os

# Это минимум который должен быть в настройках
# Для БД и секретного ключа стоит указать значения по умолчанию
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_key')


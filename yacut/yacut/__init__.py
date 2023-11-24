from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

ID_LENGHT = 6

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Эта часть импортов должна быть тут, 
# так как эти модули используют у себя экземпляры выше
from . import api_views, views

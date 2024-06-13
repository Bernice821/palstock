from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from os import path

DB_NAME = 'db'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


def create_database():
    db.create_all()
    print('Created Database!')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://username:password@localhost:3306/{DB_NAME}'
    db.init_app(app)

    from .func import func
    from .api  import api
    from .database   import database
    app.register_blueprint(database, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
    app.register_blueprint(func, url_prefix='/')

    with app.app_context():
        create_database()


    return app
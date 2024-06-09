from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from os import path
import csv

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
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:12345678@localhost:3306/{DB_NAME}'
    db.init_app(app)

    with app.app_context():
        # db.drop_all()
        create_database()

    return app
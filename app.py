import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from static.get_data_from_json import get_data_from_json
from db.check_db_connenction import test_db_connection


class Configuration:
    # The function `__init__` is the constructor of the class. This method is called
    # when an object of this class is instantiated. Here, it is being used to initialize
    # various configuration values.
    def __init__(self):
        self.secret_key = get_data_from_json("config/secret_key.json")
        sql_login_data = get_data_from_json("config/db_login.json")
        self.sql_alchemy_database_uri = f"mysql+mysqlconnector://{sql_login_data['dbusername']}:{sql_login_data['password']}@{sql_login_data['servername']}/{sql_login_data['dbname']}"
        self.sql_alchemy_track_modifications = False


config = Configuration()

app = Flask(__name__)
app.secret_key = config.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = config.sql_alchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.sql_alchemy_track_modifications

db = SQLAlchemy()
db.init_app(app)

from controller.auth import auth
from controller.admin import admin
from controller.user import user

app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(user, url_prefix="/user")

if __name__ == 'app':
    with app.app_context():
        test_db_connection(db.engine)
    app.run()

from flask import Flask
import sqlite3



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hdihhuei'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Blueprinter.config import CLIENT_ID, CLIENT_SECRET, CALLBACK_URL, SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite-latest.sqlite'
db = SQLAlchemy(app)

app.app_context().push()

from Blueprinter import routes

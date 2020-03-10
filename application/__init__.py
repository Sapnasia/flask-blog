from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('')
db = SQLAlchemy(app)

from application import routes


app.config['SECRET_KEY'] = ''
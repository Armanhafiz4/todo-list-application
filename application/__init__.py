from flask import flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.246.11.163/flask_db"

db = SQLAlchemy(app)

from application import routes

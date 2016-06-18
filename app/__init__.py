from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.restful import reqparse, Api


app = Flask(__name__)

app.config.from_object('config')
db=SQLAlchemy(app)
api = restful.Api(app)

from app import views,models
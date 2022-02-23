from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column
# creating an instance of the flask app
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'the random string'

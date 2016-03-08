from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = "this is a super secure key"

# remember to change to heroku's database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zqexxmeqqdemiv:fwE8TDtVwxklzYQk3ojJ6kwEWQ@ec2-54-83-0-187.compute-1.amazonaws.com:5432/de3sv5dg3upfl4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://project:admin@localhost/project'
db = SQLAlchemy(app)


from app import views
from app.models import Myprofile



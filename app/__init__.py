from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID, COMMON_PROVIDERS


app = Flask(__name__)

app.config['SECRET_KEY'] = "this is a super secure key"
app.config['OPENID_PROVIDERS'] = COMMON_PROVIDERS
# remember to change to heroku's database
# @TODO: app.config['SQLALCHEMY_DATABASE_URI'] = 'heroku'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project:admin@localhost/project'
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,'/tmp')

from app import views
from app.models import Myprofile



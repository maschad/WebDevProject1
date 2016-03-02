from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID, COMMON_PROVIDERS

import os
import urlparse

from sqlalchemy.dialects.postgresql import psycopg2

app = Flask(__name__)

app.config['SECRET_KEY'] = "this is a super secure key"
app.config['OPENID_PROVIDERS'] = COMMON_PROVIDERS

# remember to change to heroku's database
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,'/tmp')

from app import views
from app.models import Myprofile



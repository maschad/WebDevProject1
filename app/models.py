from . import db  
class Myprofile(db.Model):     
    id = db.Column(db.Integer, primary_key=True)     
    first_name = db.Column(db.String(80), unique=True)     
    last_name = db.Column(db.String(80), unique=True)     
    nickname = db.Column(db.String(80), unique=True)     

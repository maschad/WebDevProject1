from flask_wtf.file import FileField, FileAllowed
from wtforms import Form,SelectField,TextField,IntegerField,validators

from app import db
from app.models import Myprofile


def username_validator(form , field):
    user = db.session.query(Myprofile).filter_by(username=field.data).first()
    if user != None:
        field.errors.append('Username already taken')
        return False
    return True


class ProfileForm(Form):
     username = TextField('Username', [username_validator,validators.Length(min=4, max=25)])
     first_name = TextField('First Name', [validators.Length(min=4, max=25)])
     last_name = TextField('Last Name', [validators.Required()])
     age = IntegerField('Age',[validators.Required()])
     sex = SelectField('Sex',choices=[('M','Male'),('F','Female')])
     image = FileField('Image File',[FileAllowed(['jpg', 'png'], 'Images only!')])


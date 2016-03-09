from wtforms import Form,SelectField,TextField,SubmitField,PasswordField,IntegerField,validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ProfileForm(Form):
     username = TextField('Username', validators=[validators.username_validator()])
     first_name = TextField('First Name', [validators.Required()])
     last_name = TextField('Last Name', [validators.Required()])
     age = IntegerField('Age',[validators.Required()])
     sex = SelectField('Sex',choices=[('M','Male'),('F','Female')])
     image = FileField('Image File',validators =[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
     submit = SubmitField("Send")

def username_validator(form , field):
    user = db.session.query(User).filter_by(username=field.data).first()
    if user != None:
        field.errors.append('Username already taken')
        return False
    return True
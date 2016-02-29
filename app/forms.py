from wtforms import Form,SelectField,TextField,SubmitField,PasswordField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ProfileForm(Form):
     username = TextField('Username', [validators.Length(min=2, max=25)])
     first_name = TextField('First Name', [validators.Required()])
     last_name = TextField('Last Name', [validators.Required()])
     age = TextField('Age',[validators.Required()])
     sex = SelectField('Sex',choices=[('M','Male'),('F','Female')])
     image = FileField('Image File',validators =[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
     submit = SubmitField("Send")


class LoginForm(Form):
     username = TextField('Username', validators.Required())
     password= PasswordField('Password', validators.Required())

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

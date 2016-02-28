from flask.ext.wtf import Form
from flask.ext.wtf.file import FileAllowed,FileRequired
from wtforms.fields import TextField,PasswordField,SelectField,FileField,SubmitField # other fields include PasswordField
from wtforms.validators import Required, Email


class ProfileForm(Form):
     username = TextField('Username', validators=[Required()])
     first_name = TextField('First Name', validators=[Required()])
     last_name = TextField('Last Name', validators=[Required()])
     age = TextField('Age',validators=[Required()])
     sex = SelectField('Sex',choices=[('M','Male'),('F','Female')])
     image = FileField(u'Image File',validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
     submit = SubmitField("Send")


class LoginForm(Form):
     username = TextField('Username', validators=[Required()])
     password= PasswordField('Password', validators=[Required()])
    
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

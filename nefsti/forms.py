from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField,SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField,FileAllowed,file_required

class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    username = StringField("Username",validators=[DataRequired(message="your username is required")])
    email = StringField("Your Email",validators=[Email()])
    password = PasswordField("password", validators=[DataRequired()])
    phone_number= StringField("Phone Number",validators=[DataRequired()])
    house_address= StringField("House Address",validators=[DataRequired()])
    confirm_password = PasswordField("confirm password", validators=[EqualTo('password',message='confirm password must be equal to password')])
    btn = SubmitField("sign up!")
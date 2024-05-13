from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Length,InputRequired

class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    login_id = StringField('Login ID', validators=[DataRequired(), Length(max=50)])
    user_name = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    horoscope_sign = StringField('Horoscope Sign', validators=[Length(max=50)])
    city = StringField('City', validators=[Length(max=50)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """Form for registering a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
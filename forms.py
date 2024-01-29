from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    login_id = StringField('Login ID', validators=[DataRequired(), Length(max=50)])

    horoscope_sign = StringField('Horoscope Sign', validators=[Length(max=50)])
    city = StringField('City', validators=[Length(max=50)])
    submit = SubmitField('Register')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    choose = StringField('Poke', validators = [DataRequired()])

    submit = SubmitField()
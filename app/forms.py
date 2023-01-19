from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    choice = StringField('Pokemon', validators = [DataRequired()])

    submit = SubmitField()
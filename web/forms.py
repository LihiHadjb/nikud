from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class InputText(FlaskForm):
    input = TextAreaField()
    submit = SubmitField('נקד לי!')


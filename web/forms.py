from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class InputText(FlaskForm):
    input = TextAreaField()
    submit = SubmitField('נקד לי!')


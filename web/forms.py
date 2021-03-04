from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email


class InputText(FlaskForm):
    input = TextAreaField()
    submit = SubmitField()


#TODO: put the label to the right of the field
class ContactForm(FlaskForm):
    type = SelectField(
        'סוג הפנייה',
        [DataRequired()],
        choices=[
            ('bug', 'דיווח על באג'),
            ('suggestion', 'הצעה לשיפור'),
            ('other', 'סתם בא לי לדבר')
        ]
    )

    content = TextAreaField()
    email = StringField(
        'Email',
        [
            Email(message='כתובת המייל אינה תקנית'),
        ]
    )
    submit = SubmitField()


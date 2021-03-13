from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

#from ..models import Employee


class AudioForm(FlaskForm):
    """
    Form for users to create new audio
    """
    name = StringField('name', validators=[DataRequired(), ])
    duration = IntegerField('duration', validators=[DataRequired(),Length(min=1,max=100),])
    host = StringField('host', validators=[Length(min=1,max=100)])
    initators = StringField('Last Name', validators=[Length(min=1,max=100)])
    submit = SubmitField('Send')




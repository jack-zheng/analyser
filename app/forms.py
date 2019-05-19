from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PlayGroundForm(FlaskForm):
    '''
    Form for play ground demo. in this class, we accept input and show it
    on page after submit
    '''
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message',
                         validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()

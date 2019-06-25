from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, \
    BooleanField
from wtforms.validators import DataRequired, Length, Email


class PlayGroundForm(FlaskForm):
    '''
    Form for play ground demo. in this class, we accept input and show it
    on page after submit
    '''
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message',
                         validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()


class UpdateForm(FlaskForm):
    '''
    Form that used to trigger update of github history manually.
    '''
    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class JQueryForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class RegisterProvisioner(FlaskForm):
    inumber = StringField(
        'I Number', validators=[DataRequired(), Length(1, 20)])
    email = StringField(
        'Email', validators=[DataRequired(), Length(1, 128), Email()])
    submit = SubmitField('Register')


class MapCompany(FlaskForm):
    inumber = StringField(
        'I Number', validators=[DataRequired(), Length(1, 20)])
    company = StringField(
        'Company Id', validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField('Submit')

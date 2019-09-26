from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, DateTimeField, TextAreaField 
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange



class AddRunForm(FlaskForm):
    distance = DecimalField('Distance [km]', validators=[DataRequired()])
    duration_h = DecimalField('Duration [hh:mm:ss]', validators=[NumberRange(min=0)])
    duration_m = DecimalField('Duration', validators=[NumberRange(min=0, max=59)])
    duration_s = DecimalField('Duration', validators=[NumberRange(min=0, max=59)])
    timestamp = DateTimeField('Run Date/Time', format='%d/%m/%Y')
    submit = SubmitField('Submit')

    
class AddInjuryForm(FlaskForm):
    title = StringField('Injury type', validators=[DataRequired()])
    description = TextAreaField('Description [optional]')
    timestamp = DateTimeField('Injury Date', format='%d/%m/%Y')
    submit = SubmitField('Submit')
    
    
class EditUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
#    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Update')
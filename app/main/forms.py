from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange



class AddRunForm(FlaskForm):
    distance = DecimalField('Distance [km]', validators=[DataRequired()])
    duration_h = DecimalField('Duration [hh:mm:ss]', validators=[NumberRange(min=0)])
    duration_m = DecimalField('Duration', validators=[NumberRange(min=0, max=59)])
    duration_s = DecimalField('Duration', validators=[NumberRange(min=0, max=59)])
    timestamp = DateTimeField('Run Date/Time', format='%d/%m/%Y')
    submit = SubmitField('Submit')

    
class AddInjuryForm(FlaskForm):
    distance = DecimalField('Distance', validators=[DataRequired()])
    time = DecimalField('Time', validators=[DataRequired()])
    timestamp = DateTimeField('Injury Date/Time')
    submit = SubmitField('Submit')
    
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
#from wtforms.validators import DataRequired, Email, EqualTo, Length
#
#
#
#class LoginForm(FlaskForm):
#    username = StringField('Username', validators=[DataRequired()])
#    password = PasswordField('Password', validators=[DataRequired()])
#    submit = SubmitField('Login')
#    
#    
#class RegisterForm(FlaskForm):
#    username = StringField('Username', validators=[DataRequired()])
#    email = StringField('Email', validators=[DataRequired(), Email()])
#    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
#    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
#    submit = SubmitField('Register')
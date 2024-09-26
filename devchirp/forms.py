from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from devchirp.models import User, 


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#raising  custom  validation error for users trying  to register with the same username
    def validate_username(self, username):
        if  username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()# check if the username already exists in the database 
            if user:
                raise ValidationError('User already exist')

# raising custom validation error for users trying to register with the same email
    def validate_email(self, email):
        if  email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exist')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    remember_password = BooleanField('Remember Me')
    submit = SubmitField('Log in')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Profile')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
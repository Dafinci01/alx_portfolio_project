# Import FlaskForm from the flask_wtf package to create web forms in Flask applications
from flask_wtf import FlaskForm
# Import various fields and validators from wtforms for creating form fields and validating user input
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo  # Validators to regulate input, like email format, required fields, etc.

# Configure a secret key for the Flask application to prevent CSRF (Cross-Site Request Forgery) attacks
#app.config['SECRET_KEY'] = '6a031eb93693472f4d44bb82ddb5dad8'  
# Define the registration form by creating a class that inherits from FlaskForm
class RegistrationForm(FlaskForm):
    # Username field with validation: must be provided (DataRequired) and should be between 2 and 20 characters
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # Email field with validation: must be provided and must be a valid email address
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Password field with validation: must be provided
    password = PasswordField('Password', validators=[DataRequired()])

    # Confirm Password field with validation: must be provided and must match the 'password' field
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) 
    # Submit button to submit the registration form
    submit = SubmitField('Sign Up')

# Define the login form by creating a class that inherits from FlaskForm
class LoginForm(FlaskForm):
    # Email field with validation: must be provided and must be a valid email address
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Password field with validation: must be provided
    password = PasswordField('Password', validators=[DataRequired()])

    # Checkbox for "Remember Me" functionality, allowing the user to stay logged in
    remember_password = BooleanField('Remember Me')

    # Submit button to submit the login form
    submit = SubmitField('Log in')

# Note: After creating forms, you need to create a secret key to prevent malicious attacks.
# You can use the following line of code to generate a secret key:
# app.config['SECRET_KEY'] = ''

# Then, generate a secret key from the Python command line (or other secure methods).


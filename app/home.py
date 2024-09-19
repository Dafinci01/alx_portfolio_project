from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import LoginForm, RegistrationForm
import os  # <-- Add this import for working with file paths

app = Flask(__name__)


# SQLAlchemy instance created 
db = SQLAlchemy(app)

# Configure a secret key for the Flask application to prevent CSRF (Cross-Site Request Forgery) attacks
app.config['SECRET_KEY'] = '6a031eb93693472f4d44bb82ddb5dad8'
#app.config['SQLALCHEMY_DATABASE _URI'] = 'sqlite:///instance/site.db'
# Use absolute path for the SQLite database
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'site.db')

# Create user model for the app
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Create post model for the app
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# Dummy data for posts
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'David Odelana',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, url_for, flash, redirect, request
from devchirp import db, app, bcrypt
from devchirp.models import User, Post
from devchirp.forms  import RegistrationForm, LoginForm, PostForm, UpdateProfileForm  # Import your database setup here
from flask_login import login_user, current_user, logout_user, login_required
from  sqlalchemy.exc import IntegrityError
import requests

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
    #write acomment ehere 
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

#route to register new users 
@app.route("/register", methods=['GET', 'POST'])
def register():
    #logic to make user that has login not log out 
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
    #check if tge email already exists im the database 
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email already exists', 'danger')
            return redirect(url_for('register'))
        #added bcrypt passsword hashingto protect userd  from gettinmg hacked 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    #logic to make user that has login not log out 
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
       #logic for logging in a user (1) first of all, query the database to check whether user exist
       user = User.query.filter_by(email=form.email.data).first() #if user database eqauls to what user enters into data
       # aconditional that verify if the passsword enter  verifies with what they enter into  databse 
       if user and  bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
       else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


def add_new_user(username, email, password, image_file = 'default.jpg'):
    #check if a user with the same username or email already exists
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)).first()
    if existing_user:
        return "User already exists"
    try :
        new_user = User(username=username, email=email, password=password, image_file=image_file)
        db.session.add(new_user)
        db.session.commit()
        return "User added successfully"
    except IntegrityError:
        db.session.rollback()
        return "An error occurred"

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/post/new", methods=['GET', 'POST'])
@login_required 
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)  # Create new post
        db.session.add(post)
        db.session.commit()  # Save post to database
        flash('Your post has been created!', 'success')  # Success message after post creation
        return redirect(url_for('home'))  # Redirect to home page after creating post
    return render_template('create_post.html', title='New Post', form=form)

@app.route("/account", methods=['GET', 'POST'])
@login_required 
def account():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()  # Update changes to database
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))  # Reload the account page
    form.username.data = current_user.username
    form.email.data = current_user.email
    return render_template('account.html', title='Account')

@app.route('/github_stats/<username>')
def github_stats(username):
    #bas
    github_user_url = f"https://api.github.com/users/{username}"  # GitHub API URL for fetching user data
    github_repos_url = f"https://api.github.com/users/{username}/repos"  # GitHub API URL for fetching user repositories
    

    # fetch user data
    user_response = requests.get(github_user_url)
    repos_response = requests.get(github_repos_url)
    
    if user_response.status_code == 200 and repos_response.status_code== 200:
        user_data = user_response.json()  # Convert the response to JSON format
        repos_data = repos_response.json()  # Convert the response to JSON format
        return render_template('github_stats.html', user=user_data, repos=repos_data)  # Pass the GitHub user data to the template
    else:
        flash('GitHub user not found', 'danger')
        return redirect(url_for('home'))

#@app.route("/account")
#def account():
   # return render_template('account.html', title='Account')
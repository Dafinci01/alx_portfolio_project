from flask import render_template, url_for, flash, redirect, request
from devchirp import db, app
from devchirp.models import User, Post
from devchirp.forms  import RegistrationForm, LoginForm, PostForm, UpdateProfileForm  # Import your database setup here
from flask_login import login_user, current_user, logout_user, login_required
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
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
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
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

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
    return render_template('account.html', title='Account', form=form)

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


from flask import Flask, render_template, url_for, flash, redirect, request
from alx_portfolio_project.database import db  # Import db directly, no need to initialize again
from alx_portfolio_project.forms import LoginForm, RegistrationForm, PostForm#, UpdateProfileForm
  # Ensure this is below the db initialization
from flask_login import login_user, current_user, logout_user, login_required
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '6a031eb93693472f4d44bb82ddb5dad8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)  # Use init_app to tie db to the app
from .model import User, Post  

# Ensure the app context is available for running db commands
with app.app_context():
    db.create_all()  # This will create all tables if they don't exist yet

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
    posts = Post.query.order_by(Post.data_posted.desc()).paginate(page=page,per_page=5)
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

#Log_out route 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#route for creating nrew posts (re)
@app.route("/post/new", methods=['GET', 'POST'])
@login_required 
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data,author=current_user) #create new post
        db.session.add(post)
        db.session.commit()# save post to database
        flash('your post has been created!, succcess') # success message after post creation 
        return redirect(url_for('home'))#redirect to home page after creating psot 
    return render_template('create_post.html', title='New Post', form=form)

#user profile update route 
@app.route("/account", methods=['GET', 'POST'])
@login_required 
def account():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data 
        current_user.email = form.email.data 
        db.session.commit() #update changes to database 
        return redirect(url_for('account'))#reload the account pade 
    form.username.data = current_user.username
    form.email.data = current_user.user.email


#github stats inteegration route
@app.route('/github_stats/<username>')
def github_stats(username):
    github_api_url=f"https://api.github.com/users/{username}"# github api url for fetching user data 
    response = requests.get(github_api_url)
    if response.status == 200:
        user.data = response.json() #convert the response to json format 
        return render_template('github_stats.html', user=user_data)# pass the github user data to the template 
    
    else:
        flash('Github user not found', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

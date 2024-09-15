from flask import Flask, render_template, url_for, flash, redirect
from app.forms import LoginForm, RegistrationForm

app = Flask(__name__)
# Configure a secret key for the Flask application to prevent CSRF (Cross-Site Request Forgery) attacks
app.config['SECRET_KEY'] = '6a031eb93693472f4d44bb82ddb5dad8'

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
            flash('you have beeen  logged in!', 'success')
            return redirect(url_for('home'))
        else:
             flash('Login Unsuuccesful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

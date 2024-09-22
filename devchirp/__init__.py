from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '6a031eb93693472f4d44bb82ddb5dad8'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db= SQLAlchemy(app)  # Initialize the database

#with app.app_context():
#    db.create_all()  # This will create all tables if they don't exist yet
#from . import routes  # Import routes after app is defined
                                                   
from devchirp import routes
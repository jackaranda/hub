# Import flask and template operators
from flask import Flask, render_template

# Import python-social-auth 
from social_flask.routes import social_auth
from social_flask_sqlalchemy.models import init_social

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__, static_url_path='/assets', static_folder='./web/assets/')

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Initialize social auth db
init_social(app, db)

# Sample HTTP error handling
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.auth.controllers import auth
from app.web.controllers import web

# Register blueprint(s)
app.register_blueprint(social_auth)
app.register_blueprint(auth)
app.register_blueprint(web)

db.create_all()
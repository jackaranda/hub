from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

import flask_login
login_manager = flask_login.LoginManager()

from flask import current_app


from .models import Account

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@login_manager.user_loader
def load_user(email):

    with current_app.Session.begin() as session:
        users = session.query(Account).filter_by(email=email).all()
    
    return users[0]

# Sign up
@auth.route('/signup', methods=['GET', 'POST'])
def auth_signup():

    current_app.logger.debug('signup')

    if request.method == 'POST':
        current_app.logger.debug('Got POST on /signup')
        current_app.logger.debug(request.form['email'])

    return render_template("auth/signup.html")

# Set the route and accepted methods
@auth.route('/login', methods=['GET'])
def auth_root():
    return render_template("auth/auth.html")


# Set the route and accepted methods
@auth.route('/account/<shortname>', methods=['GET'])
def auth_account(shortname):
    return render_template("auth/account.html")


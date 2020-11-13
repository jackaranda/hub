from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for



# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@auth.route('/login', methods=['GET'])
def auth_root():
    return render_template("auth.html")

# Set the route and accepted methods
@auth.route('/account/<shortname>', methods=['GET'])
def auth_account(shortname):
    return render_template("account.html")


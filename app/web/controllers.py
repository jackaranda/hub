from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for



# Define the blueprint: 'auth', set its url prefix: app.url/auth
bp_web = Blueprint('web', __name__, url_prefix='/')

# Set the route and accepted methods
@bp_web.route('/', methods=['GET'])
def index():
    return render_template("index.html")
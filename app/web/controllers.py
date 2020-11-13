from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from flask import jsonify

# Define the blueprint: 'auth', set its url prefix: app.url/auth
web = Blueprint('web', __name__, url_prefix='/', template_folder='templates')

# Set the route and accepted methods
@web.route('/', methods=['GET'])
def index():
    return render_template("web/index.html", message="Hobo")

@web.route('/maps/<shortname>', methods=['GET'])
def maps(shortname):
    return render_template("web/maps.html", shortname=shortname)

@web.route('/maps/<shortname>/features', methods=['GET'])
def map_features(shortname):
    with open('data/maps/{}/features.json'.format(shortname)) as fp:
        return fp.read()


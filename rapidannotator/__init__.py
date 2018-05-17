from flask import Flask
app = Flask(__name__)
app.config.from_object('rapidannotator.config.DevelopmentConfig')

from flask_login import LoginManager
login = LoginManager()
login.login_view = 'frontpage'
login.init_app(app)

from rapidannotator.models import db
db.init_app(app)
'''
    .. for creating all the required tables
'''
with app.app_context():
    db.create_all()

from rapidannotator.modifyJsonEncoder import JSONEncoder
app.json_encoder = JSONEncoder

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


'''
    ..import all the blueprints
'''
from rapidannotator.modules.frontpage import blueprint as frontpage
app.register_blueprint(frontpage, url_prefix='/frontpage')

from rapidannotator.modules.home import blueprint as home
app.register_blueprint(home, url_prefix='/home')

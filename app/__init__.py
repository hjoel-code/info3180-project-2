from flask import Flask
from .config import Config

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect



app = Flask(__name__, static_folder='../dist/assets')
csrf = CSRFProtect(app)
app.config.from_object(Config)



# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import views
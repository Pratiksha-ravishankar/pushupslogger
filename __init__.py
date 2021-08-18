#first file that runs on execution
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

db = SQLAlchemy()

def create_app():
    app=Flask(__name__)

    #connecting flask to db
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # connecting main.py to __init__.py
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #connecting auth.py to __init__.py
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

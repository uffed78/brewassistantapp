from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

from .models import db  # Importera db här

db = SQLAlchemy()  # Databasen initieras här

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brewassistant.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'

    Session(app)  # Sessionshantering
    db.init_app(app)  # Koppla databasen till appen

    with app.app_context():
        from .routes import main, auth, brewfather, gpt
        app.register_blueprint(main.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(brewfather.bp)
        app.register_blueprint(gpt.bp)
        db.create_all()  # Skapa databastabeller

    return app

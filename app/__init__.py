from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

from app.models.models import db  # Importera db från models

def create_app():
    app = Flask(__name__)
    
    # Flask-konfigurationer
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brewassistant.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'

    # Initiera session och databas
    Session(app)
    db.init_app(app)

    # Registrera Blueprints
    with app.app_context():
        from app.routes import main, auth, brewfather, gpt  # Importera routes
        app.register_blueprint(main.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(brewfather.bp)
        app.register_blueprint(gpt.bp)
        db.create_all()  # Skapa databastabeller

    return app

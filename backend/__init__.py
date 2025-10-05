import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """Application factory function."""
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS to allow your React frontend to make requests to the backend
    CORS(app)

    # Load configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a-dev-secret-key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'a-dev-jwt-key')

    # Configure the database
    # For Render, it will use the DATABASE_URL environment variable.
    # For local dev, it falls back to a SQLite database in the 'instance' folder.
    default_db_path = f"sqlite:///{os.path.join(app.instance_path, 'db.sqlite3')}"
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', default_db_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions with the app
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        # Import models here to ensure they are registered with SQLAlchemy
        from . import models

        # Import Blueprints
        from .routes.users_routes import users_bp
        # from .routes.tracks_routes import tracks_bp
        # from .routes.track_links_routes import track_links_bp

        # Register Blueprints with URL prefixes
        app.register_blueprint(users_bp, url_prefix='/api/users')
        # app.register_blueprint(tracks_bp, url_prefix='/api/tracks')
        # app.register_blueprint(track_links_bp, url_prefix='/api/track_links')

        # Create database tables for our models
        db.create_all()

    return app  # ← Move this line outside the 'with' block
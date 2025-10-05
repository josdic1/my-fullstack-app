import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    """Application factory function."""
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS
    CORS(app)

    # Load configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a-dev-secret-key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'a-dev-jwt-key')

    # Configure the database
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

    # Add a simple test route directly here
    @app.route('/')
    def health_check():
        return {'status': 'ok', 'message': 'Flask app is running'}
    
    @app.route('/api/test', methods=['GET'])
    def test_db():
        try:
            db.session.execute(db.text('SELECT 1'))
            return {'message': 'DB Connection Success!'}, 200
        except Exception as e:
            return {'error': f'DB Connection Failed: {str(e)}'}, 500

    with app.app_context():
        from . import models
        from .routes.users_routes import users_bp
        
        app.register_blueprint(users_bp, url_prefix='/api/users')
        db.create_all()

    return app  # CRITICAL: This must be OUTSIDE the 'with' block
from flask import jsonify
from backend import db  # Import db from backend package

def register_routes(app):
    @app.route('/api/test', methods=['GET'])
    def test_db():
        try:
            db.session.execute('SELECT 1')  # Use db.session instead of app.config
            return jsonify({'message': 'DB Connection Success!'}), 200
        except Exception as e:
            return jsonify({'error': f'DB Connection Failed: {e}'}), 500
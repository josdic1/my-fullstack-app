# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # SQLite for simplicity
# For PostgreSQL: app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/myapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/test')
def test_db():
    try:
        db.session.execute('SELECT 1')
        return "DB Connection Success!"
    except Exception as e:
        return f"DB Connection Failed: {e}"
    
# routes #
@app.route('/api/data')
def get_data():
    return jsonify({"message": "This data came from the Flask backend!"})
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
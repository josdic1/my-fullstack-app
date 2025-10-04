import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS 

load_dotenv() # Load environment variables from .env

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
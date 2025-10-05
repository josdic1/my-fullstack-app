from flask import Blueprint, request, jsonify
from backend import db
from backend.models import Track

tracks_bp = Blueprint('tracks_bp', __name__)

@tracks_bp.route('/', methods=['GET'])
def list_tracks():
    tracks = Track.query.all()
    return jsonify([t.to_dict() for t in tracks])

@tracks_bp.route('/', methods=['POST'])
def create_track():
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({'error': 'title is required'}), 400
    track = Track(title=title, artist=data.get('artist'), genre=data.get('genre'), user_id=data.get('user_id') or 1)
    db.session.add(track)
    db.session.commit()
    return jsonify(track.to_dict()), 201

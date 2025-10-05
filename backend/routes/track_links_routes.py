from flask import Blueprint, request, jsonify
from backend import db
from backend.models import TrackLink

track_links_bp = Blueprint('track_links_bp', __name__)

@track_links_bp.route('/', methods=['GET'])
def list_links():
    links = TrackLink.query.all()
    return jsonify([l.to_dict() for l in links])

@track_links_bp.route('/', methods=['POST'])
def create_link():
    data = request.get_json() or {}
    track_id = data.get('track_id')
    link_type = data.get('link_type')
    link_url = data.get('link_url')
    if not all([track_id, link_type, link_url]):
        return jsonify({'error': 'track_id, link_type and link_url required'}), 400
    link = TrackLink(track_id=track_id, link_type=link_type, link_url=link_url)
    db.session.add(link)
    db.session.commit()
    return jsonify(link.to_dict()), 201

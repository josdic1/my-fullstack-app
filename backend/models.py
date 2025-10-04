from .app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        """Hash and store the password."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify the password against the stored hash."""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
        }
    

class Track(db.Model):
    __tablename__ = 'track'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120), nullable=True)
    genre = db.Column(db.String(120), nullable=True)

    tracks_links = db.relationship('TrackLink', backref='track', lazy=True)

    def __repr__(self):
        return f'<Track {self.title} by {self.artist}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'genre': self.genre,
        }
    
class TrackLink(db.Model):
    __tablename__ = 'track_link'
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)
    link_type = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<TrackLink {self.link_url} for Track ID {self.track_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'track_id': self.track_id,
            'link_type': self.link_type,
            'link_url': self.link_url,
        }

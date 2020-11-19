from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rating(db.Model):
    """A movie rating"""

    __tablename__ = 'ratings'

    movie_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    movie_title = db.Column(db.String)                    
    thumbs_up = db.Column(db.Integer)
    thumbs_down = db.Column(db.Integer)

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
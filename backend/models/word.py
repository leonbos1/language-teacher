from datetime import datetime
from extensions import db
from flask_restful import fields

class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.String(255), nullable=False)
    italian = db.Column(db.String(255), nullable=False)
    dutch = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, english, italian, dutch):
        self.english = english
        self.italian = italian
        self.dutch = dutch

    def __repr__(self):
        return '<Word %r>' % self.english


word_fields = {
    'id': fields.Integer,
    'english': fields.String,
    'italian': fields.String,
    'dutch': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
}

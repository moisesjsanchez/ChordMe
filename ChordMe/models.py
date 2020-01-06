from ChordMe import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(80), nullable=True)
    admin = db.Column(db.Boolean)
    public_id = db.Column(db.String(50), unique=True)


class Chord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    string_names = db.Column(db.String, nullable=False)
    chord_name = db.Column(db.String, nullable=False)

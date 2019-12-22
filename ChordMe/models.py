from ChordMe import db
from flask import current_app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)

class Chord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    string_names = db.Column(db.String, nullable=False)
    chord_name =  db.Column(db.String, nullable=False)
from flask import Flask, jsonify, json, Blueprint, request
from ChordMe import db
from ChordMe.models import Chord

user = Blueprint('user', __name__)

#api for registered users chord manipulation 
@user.route('/my-chords')
def test():
    return ""

@user.route('/user', methods=['GET'])
def select_chord():
    return ""

@user.route('/user', methods=['POST'])
def create_chord():
    chord_data = request.get_json()

    new_chord = Chord(chord_name=chord_data['chord_name'], string_names=chord_data['string_names'], 
    notes=chord_data['notes'])

    db.session.add(new_chord)
    db.session.commit()

    return 'Done', 201

@user.route('/user', methods=['PUT'])
def edit_chord():
    return ""

@user.route('/user', methods=['DELETE'])
def delete_chord():
    return ""
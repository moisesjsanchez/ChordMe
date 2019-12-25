from flask import Flask, jsonify, json, Blueprint, request
from ChordMe import db
from ChordMe.models import Chord

user = Blueprint('user', __name__)

#api for registered users chord manipulation 
@user.route('/user/<id>', methods=['GET'])
def select_chord(id):
    chord = Chord.query.filter_by(id=id).first()

    if not chord:
        return jsonify({'message':'chord not found'}), 404
    
    chord_data = {}
    chord_data['id'] = chord.id
    chord_data['notes'] = chord.notes
    chord_data['string_names'] = chord.string_names
    chord_data['chord_name'] = chord.chord_name

    return jsonify({'chords': chord_data}), 200

@user.route('/user', methods=['GET'])
def select_chords():
    chords = Chord.query.all()

    output = []
    for chord in chords:
        chord_data = {}
        chord_data['id'] = chord.id
        chord_data['notes'] = chord.notes
        chord_data['string_names'] = chord.string_names
        chord_data['chord_name'] = chord.chord_name
        output.append(chord_data)

    return jsonify({'chords': output}), 200

@user.route('/user', methods=['POST'])
def create_chord():
    chord_data = request.get_json()

    new_chord = Chord(chord_name=chord_data['chord_name'], string_names=chord_data['string_names'], 
    notes=chord_data['notes'])

    db.session.add(new_chord)
    db.session.commit()

    return jsonify({'message':'Chord has been created'}), 201

@user.route('/user/<id>', methods=['PUT'])
def edit_chord(id):

    chord = Chord.query.filter_by(id=id).first()
    
    if not chord:
        return jsonify({'message':'chord not found'}), 404
    
    notes = request.json['notes']
    string_names = request.json['string_names']
    chord_name = request.json['chord_name']

    chord.notes = notes
    chord.string_names = string_names
    chord.chord_name = chord_name

    db.session.commit()

    return jsonify({'message':'Chord has been edited'}), 200

@user.route('/user/<id>', methods=['DELETE'])
def delete_chord(id):
    chord = Chord.query.filter_by(id=id).first()
    
    if not chord:
        return jsonify({'message':'chord not found'}), 404
    
    db.session.delete(chord)
    db.session.commit()

    return jsonify({'message':'Chord has been deleted'}),200
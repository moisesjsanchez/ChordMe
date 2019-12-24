from flask import Flask, jsonify, json, Blueprint, request
from ChordMe import db
from ChordMe.models import Chord

user = Blueprint('user', __name__)

#api for registered users chord manipulation 
@user.route('/user', methods=['GET'])
def select_chord():
    chord = Chord.query.filter_by(id=id).first()

    if not chord:
        return jsonify('message':'chord not found')
        
    chord_data['id'] = chord.id
    chord_data['notes'] = chord.notes
    chord_data['string_names'] = chord.string_names
    chord_data['chord_name'] = chord.chord_name
    
    output.append(chord_data)

    return jsonify({'chords': output})

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

    return jsonify({'chords': output})

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

    chord = Chord.query.filter_by(id=id).first()

    if not chord:
        return jsonify('message':'chord not found')
    
    chord = Chord(chord_name=chord_data['chord_name'], string_names=chord_data['string_names'], 
    notes=chord_data['notes'])
    db.session.commit()

    return jsonify('message':'Chord has been edited')

@user.route('/user', methods=['DELETE'])
def delete_chord():

    chord = Chord.query.filter_by(id=id).first()
        if not chord:
        return jsonify('message':'chord not found')
    
    db.session.delete(chord)
    db.session.commit()

    return jsonify('message':'Chord has been deleted')
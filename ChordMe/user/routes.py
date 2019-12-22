from flask import Flask, jsonify, json, Blueprint, Response
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
    return ""

@user.route('/user', methods=['PUT'])
def edit_chord():
    return ""

@user.route('/user', methods=['DELETE'])
def delete_chord():
    return ""
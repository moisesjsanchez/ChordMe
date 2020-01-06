from ChordMe import db
from ChordMe.models import User
from ChordMe.auth.token import token_required
from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import uuid
import datetime

auth = Blueprint('auth', __name__)

# Search User Accounts
@auth.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):

    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.end(user_data)

    return jsonify({'users': output})


@auth.route('/user/<public_id>', methods=['GET'])
@token_required
def get_all_user(current_user, public_id):

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user': user_data})

# Register Account
@auth.route('/user', methods=['POST'])
@token_required
def create_user(current_user):

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(
        uuid.uuid4()), username=data['username'], email=data['email'],
        password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})

# Promote User
@auth.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found'})

    user.admin = True
    db.session.commit()

    return jsonify({'message': 'The user has been promoted'})

# Delete user
@auth.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user has been deleted'})

# Login In User
@auth.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401,
                             {'WWW-Authenticate':
                              'Basic realm = "Login in required"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401,
                             {'WWW-Authenticate':
                              'Basic realm = "Login in required"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id,
                            'exp': datetime.datetime.utcnow(
                            )+datetime.timedelta(minutes=30)}, 'SECRETKEY')
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401,
                         {'WWW-Authenticate':
                          'Basic realm = "Login in required"'})

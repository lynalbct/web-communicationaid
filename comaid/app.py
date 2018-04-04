from flask import Flask, jsonify, request,render_template, make_response
from flask import render_template, redirect, url_for, flash, request, session
from model import *
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_basicauth import BasicAuth
from flask_cors import CORS
import uuid

app = Flask(__name__)
db = SQLAlchemy(app)
basic_auth = BasicAuth(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:walakokahibaw@localhost/db'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/communicationaid')
def communicationaid():
    return render_template('login.html')
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token= request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing'}),
        try:
            data = jwt.decode(token), app.config['SECRET_KEY']
            current_user = Account.query.filter_by(username=data['username']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(current_user, *args,**kwargs)
    return decorated



@app.route('/user',methods=['GET'])

def getallusers():
	users = Account.query.all()

	output= []
	for user in users :
		user_data = {}
		user_data['acc_id'] = user.acc_id
		user_data['username'] = user.username
		user_data['email'] = user.email
		user_data['acc_type'] = user.acc_type
		output.append(user_data)
	return jsonify({'users': output})

@app.route('/user/<acc_id>', methods=['GET'])
def getoneuser(acc_id):
	user = Account.query.filter_by(acc_id=acc_id).first()
	if not user: 
		return jsonify ({'message': 'no user found'})
	user_data = {}
	user_data['acc_id'] = user.acc_id
	user_data['username'] = user.username
	user_data['email'] = user.email
	user_data['acc_type'] = user.acc_type
	user_data['password'] = user.password
	return jsonify ({'user' : user_data})

@app.route('/user', methods=['POST'])
def createuser():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	new_acc = Account(acc_type=str(uuid.uuid4()), username = data['username'],email=data['email'], password = hashed_password)
	db.session.add(new_acc)
	db.session.commit()
	return jsonify({'message' : 'New user created.'})

@app.route('/user/<acc_id>', methods=['PUT'])
def updateuser():
	return ''

@app.route('/user/<acc_id>', methods=['DELETE'])
@token_required
def deleteuser(acc_id):
	user =  Account.query.filter_by(acc_id=acc_id).first()
	if not user:
		return jsonify ({'message' : 'no user found'})
	db.session.delete(user)
	db.session.commit()
	return jsonify({'message': 'The user has been deleted.'})

@app.route('/login', methods=['GET'])

def login_api():
	# username = request.form['username']
	# password = request.form['password']
	# user = Account.query.filter_by(username=request.form['username']).first()
	auth = request.authorization
	if not auth or not auth.username or not auth.password:
		return make_response('un authenticated', 401, {'WWW-Authenticate' : 'Login required'})
	user = Account.query.filter_by(username=auth.username).first()

	if not user:
		return jsonify('User not found', 401, {'WWW-Authenticate' : 'Login required'})

	if check_password_hash(user.password,auth.password):
		token = jwt.encode({'account_id': Account.acc_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
		return jsonify({'status': 'ok', 'token': token.decode('UTF-8'), 'account_type': Account.acc_type})
	return make_response('Could not verify', {'WWW-Authenticate' : 'Login required'})

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		return render_template('signup.html')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
	return render_template('dashboard.html')

@app.route('/parent', methods=['GET', 'POST'])
def parent():
	return render_template('dashboard.htmlb')


if __name__=='__main__':
	app.run(debug=True)
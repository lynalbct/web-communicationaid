from flask import Flask, jsonify, request,render_template, make_response, flash
from flask import render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from model import *
from app import *


server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:walakokahibaw@localhost/db'
server.config['SECRET_KEY'] = 'hard to guess string'
db = SQLAlchemy(server)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
server = Flask(__name__)

@server.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = Account.query.filter_by(username= request.form['username']).first()

		if user is None:
			flash('Username or password invalid!')
			return redirect('/login')
		else:
			if check_password_hash(user.password_hash, request.form['password']):
				session['user'] = user.username
				session['acc_type'] = user.acc_type

			if session['acc_type'] == '1':
				return redirect(url_for('teacher'))
			elif session['acc_type'] == '2':
				return redirect(url_for('parent'))
	return render_template('login.html')
@server.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		return render_template('signup.html')



if __name__ == "__main__":
	server.run(port=8000, debug=True, host=localhost)
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from app import app
import os
from werkzeug.security import generate_password_hash, check_password_hash
import sys, flask, requests
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from SimpleHTTPServer import SimpleHTTPRequestHandler, test
# from requests.auth import HTTPBasicAuth


@app.route('/')
@cross_origin(origin='*')
def index():
	# requests.get('https://mighty-badlands-16603/api/login', auth=HTTPBasicAuth('user', 'pass')).json()
	return render_template('welcome.html')

@app.route('/parent')
@cross_origin(origin='*')
def parent():
  return render_template('p_prof.html')

# @app.route('/try')
# def request():
	


# @app.route('/register', methods =['POST'])
# def escala():
# 	username = request.form


# @server.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         if request.form['login'] == 'Sign in':

#             acc = Account.query.filter_by(username=request.form['username']).first()

#             if acc is None:
#                 flash('Username or password is invalid!')
#                 return redirect(url_for('login'))
#             else:
#                 if check_password_hash(acc.password_hash, request.form['password']):
#                     session.pop('acc_id', None)
#                     session.pop('acc_type', None)
#                     session.pop('email', None)
#                     # pops existing user data, if any!

#                     session['acc_id'] = acc.acc_id
#                     session['acc_type'] = acc.acc_type
#                     session['email'] = acc.email

#                     print session['user']


@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super(CORSHTTPRequestHandler, self).end_headers(self)

# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:8000')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from app import *
import os
from werkzeug.security import generate_password_hash, check_password_hash
import sys, flask

APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@server.route('/parent')
def parent():
	return render_template('p_prof.html')

# if __name__ == "__main__":
#     server.run(port=8000, debug=True)
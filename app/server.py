from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from app import *
import os
from werkzeug.security import generate_password_hash, check_password_hash
import sys, flask

APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@server.route('/parent', methods=['GET'])
def parent():
	if request.method == 'POST':
        return render_template('p_prof.html', myParent=myParent)

# if __name__ == "__main__":
#     server.run(port=8000, debug=True)
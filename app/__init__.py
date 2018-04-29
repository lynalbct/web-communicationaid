from flask import Flask, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_mail import Mail
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from config import dbstring
import psycopg2
from flask_compress import Compress


server = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:walakokahibaw@localhost/db'
# server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
server.config['SECRET_KEY'] = 'hard to guess string'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



mail = Mail(server)
Compress(server)
from app import server
manager = Manager(server)





# createTables()	
server.debug = True

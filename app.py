from flask import Flask, url_for, jsonify, request, render_template, send_from_directory, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import Class, Child, Account, Teacher, db
import json
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/db'
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


################################################################


@app.route('/manageclass')
def manageclass():
    manageclass = Class.query.order_by(Class.class_name).all()
    return render_template('class.html', manageclass=manageclass)


################################################################


@app.route('/addClass', methods=['POST', 'GET'])
def addClass():
    if request.method == 'POST':
        
        classes = Class.query.order_by(Class.class_name).first()
        classes.class_name = request.form['class_name']


        classes = db.session.merge(classes)
        db.session.add(classes)
        db.session.commit()
        return redirect(url_for('manageclass', classes=classes))
    else:
        return render_template('addclass.html')


################################################################


@app.route('/deleteClass/<class_name>', methods=['POST', 'GET'])
def deleteClass(class_name):
    if request.method == 'POST':
        Class = Class.query.filter_by(class_name=class_name).first()
        db.session.delete(Class)
        db.session.commit()
    return redirect(url_for('class'))


################################################################


@app.route('/students')
def students():
    students = Child.query.order_by(Child.c_id).all()
    return render_template('students.html', students=students)


################################################################


@app.route('/addstudents', methods=['POST', 'GET'])
def addstudents():
    if request.method == 'POST':

        student = Child.query.order_by(Child.c_id).first()
        student.c_id = request.form['c_id']
        student.fname_c = request.form['fname_c']
        student.lname_c = request.form['lname_c']


        student = db.session.merge(student)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students', student=student))
    else:
        return render_template('addstudent.html')
     

################################################################


@app.route('/deletestudent/<c_id>', methods=['POST', 'GET'])
def deletestudent(c_id):
    if request.method == 'POST':
        students = Child.query.filter_by(c_id=c_id).first()
        db.session.delete(students)
        db.session.commit()
    return redirect(url_for('students', class_name=class_name))


################################################################


# @app.route('/Class')
# def Class():
#     result1 = Class.query.order_by(Class.class_id).all()
#     return render_template('class.html', result1=result1)


# @app.route('/addClass', methods=['POST', 'GET'])
# def addClass():
#     if request.method == 'POST':
#         Class = request.form['class_name']
#         db.session.add(Class)
#         db.session.commit()
#         return redirect(url_for('class', Class=Class))
#     else:
#         return render_template('addclass.html')


# @app.route('/deleteClass/<class_id>', methods=['GET', 'POST'])
# def deleteClass():
#     Class = Class.query.order_by(Class.class_id)
#     if request.method == 'POST':
#         Store = request.form['storage']
#         results = Class.query.filter_by(class_id=Store).first()
#         db.session.delete(results)
#         db.session.commit()
#         Class = Class.query.order_by(Class.class_id)
#         return redirect(url_for('Class', Class=Class))
#     else:
#         return redirect(url_for('Class', Class=Class))


# @app.route('/students', methods=['GET', 'POST'])
# def students():
#     result2 = Child.query.filter_by(Child.c_id)
#     return render_template('students.html', result2=result2)


# @app.route('/addstudents', methods=['POST', 'GET'])
# def addstudents():
#     if request.method == 'POST':
#         students = request.form['c_id']
#         db.session.add(students)
#         db.session.commit()
#         return redirect(url_for('students'))
#     else:
#         return render_template('addstudent.html', students=students)


# @app.route('/deletestudent<c_id>', methods=['GET', 'POST'])
# def deletestudent():
#     students = Child.query.order_by(Child.c_id)
#     if request.method == 'POST':
#         Store = request.form['storage']
#         result = Child.query.filter_by(c_id=Store).first()
#         db.session.delete(result)
#         db.session.commit()
#         students = Child.query.order_by(students.c_id)
#         return redirect(url_for('students', students=students))
#     else:
#         return redirect(url_for('students', students=students))


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, url_for, jsonify, request, render_template, send_from_directory, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import Class, Child, Account, Teacher, db
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/db'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def spcall(qry, param, commit=False):
    try:
        dbo = model.DBconn()
        cursor = dbo.getcursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            dbo.dbcommit()
        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]),)]
    return res


# @app.route('/addstudent/', methods=['POST'])
# def students():

#     params = request.get_json()
#     c_id = params["childid"]


#     res = spcall('students', (childid), True)
#     if 'Error' in res[0][0]:
#         return jsonify({'status': 'error', 'message': res[0][0]})

#     return jsonify({'status': 'ok', 'message': res[0][0]})

# @app.route('/teacher_view', methods=['GET'])
# def studentsview():
#      res = spcall('studentsview', (), True)

#      if 'Error' in str(res[0][0]):
#          return jsonify({'status': 'error', 'message': res[0][0]})

#      recs = []
#      for r in res:
#       recs.append({"teacher": str(r[0]), "fname": str(r[1]), "lname": str(r[2])})
#      return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


# @app.route('/teacher_edit', methods=['POST'])
# def editstudents():

#     params = request.get_json()
#     fname = params["fname"]
#     mname = params["mname"]
#     lname = params["lname"]
#     bday  = params["bday"]
#     Class = params["Class"]


#     res = spcall('editstudents', (fname, mname, lname, bday, Class), True)

#     if 'Error' in res[0][0]:
#         return jsonify({'status': 'error', 'message': res[0][0]})
#     return jsonify({'status': 'ok', 'message': res[0][0]})
@app.route('/Class', methods=['GET', 'POST'])
def Class():
    db.create_all()
    result1 = Class.query.order_by(Class.class_id)
    return render_template('class.html', Class=result1, )


@app.route('/addClass', methods=['POST', 'GET'])
def addClass():
    if request.method == 'POST':
        Class = Class(request.form['c_id'])
        db.session.add(Class)
        db.session.commit()
        return redirect(url_for('class'))
    else:
        return render_template('addclass.html', Class=Class)
    # else:
    #     return render_template('addclass.html', Class=Class)


@app.route('/deleteClass<class_id>', methods=['GET', 'POST'])
def deleteClass():
    Class = Class.query.order_by(Class.class_id)
    if request.method == 'POST':
        Store = request.form['storage']
        results = Class.query.filter_by(class_id=Store).first()
        db.session.delete(results)
        db.session.commit()
        Class = Class.query.order_by(Class.class_id)
        return redirect(url_for('Class', Class=Class))
    else:
        return redirect(url_for('Class', Class=Class))


@app.route('/students', methods=['GET', 'POST'])
def students():
    db.create_all()
    result2 = Child.query.order_by(Child.c_id)
    return render_template('studenttable.html', students=result2, )


@app.route('/addstudents', methods=['POST', 'GET'])
def addstudents():
    if request.method == 'POST':
        students = Child(request.form['c_id'])
        db.session.add(students)
        db.session.commit()
        return redirect(url_for('studenttable'))
    else:
        return render_template('addstudent.html', students=students)
    # else:
    #     return render_template('addstudent.html', students=students)


@app.route('/deletestudent<c_id>', methods=['GET', 'POST'])
def deletestudent():
    students = Child.query.order_by(Child.c_id)
    if request.method == 'POST':
        Store = request.form['storage']
        result = Child.query.filter_by(c_id=Store).first()
        db.session.delete(result)
        db.session.commit()
        students = Child.query.order_by(students.c_id)
        return redirect(url_for('students', students=students))
    else:
        return redirect(url_for('students', students=students))

# if __name__ == '__main__':
#     app.run(threaded=True,debug=True)
if __name__ == "__main__":
    app.run(debug=True)
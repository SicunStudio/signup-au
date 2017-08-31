from flask import Flask, render_template
from flask import redirect, url_for, request, session, make_response
import sqlite3
import os
import logging

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/enroll/', methods=['POST', 'GET'])
def enroll():
    if request.method == "POST":
        try:
            db = sqlite3.connect(os.path.join(app.root_path, "data.db"))
            print(request.form)
            db.execute('insert into applicant values(?,?,?,?,?,?,?,?)',
                       [request.form['name'], request.form['sex'], request.form['major'],
                        request.form['contact'], request.form[
                            'firstWill'], request.form['secondWill'],
                        request.form['adjustable'], request.form['selfintroduce']])
            db.commit()
            return render_template('flag.html', flag="报名成功")
        except:
            return render_template('flag.html', flag="报名失败，请再试一次")
    else:
        return render_template("enroll.html")


@app.route('/introduce/', methods=['GET'])
def introduce():
    return render_template("introduce.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1")

from app import app
from app import classcode
from flask import render_template



@app.route('/')
@app.route('/index')
def index():
    classroom = classcode.classRoom()
    DAY, TIME = classcode.timenow()
    return render_template('index.html', classroom=classroom, DAY=DAY, TIME=TIME)



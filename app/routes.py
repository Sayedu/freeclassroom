from app import app
from app import Niggas
from flask import render_template
# import Niggas


@app.route('/')
@app.route('/index')
def index():
    classroom = Niggas.classRoom()
    DAY, TIME = Niggas.timenow()
    return render_template('index.html', classroom=classroom, DAY=DAY, TIME=TIME)



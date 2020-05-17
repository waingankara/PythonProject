from flask import Flask, render_template, request, jsonify
import sqlLightOp as slo
from datetime import datetime

# datetime object containing current date and time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert_homework',methods=['POST'])
def insert_homework():

    standard = request.json["standard"]
    division = request.json["division"]
    subject = request.json["subject"]
    doh = request.json["doh"]
    name = request.json["name"]
    toh = request.json["toh"]
    dessoh = request.json["dessoh"]
    now = datetime.now()
    homework = (standard,division,subject,doh,name,toh,dessoh,now)
    slo.create_homework(homework)
    return "Homework inserted"

@app.route('/create_db')
def create_db():
    slo.main()
    return "Database Operation Done"

@app.route('/all_homeworks')
def all_homeworks():
    rows = slo.select_all_homeworks()
    return rows



if __name__ == '__main__':
    app.run(debug=True)
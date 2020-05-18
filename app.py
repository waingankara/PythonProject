from flask import Flask, render_template, request, Response
import postgreOp as slo
from datetime import datetime
import csv
from io import StringIO
import time

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
    slo.create_tables()
    return "Database Operation Done"

@app.route('/all_homeworks')
def all_homeworks():

    data = StringIO()
    w = csv.writer(data)
    log = slo.get_homeworks()
    # write header
    w.writerow(['srNo', 'standard', 'division','subject','date_of_homework','teacher_name','type_of_homework','desc_of_homework','upload_date'])
    w.writerows(log)

    filename = 'output' + time.strftime("%Y%m%d%H%M%S") + '.csv'
    response = Response(data.getvalue(), mimetype='text/csv')
    # add a filename
    response.headers.set("Content-Disposition", "attachment", filename=filename)
    return response

if __name__ == '__main__':
    app.run(debug=True)
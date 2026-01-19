from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = 'http://localhost:9000'

app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    return render_template('index.html', day_of_week = day_of_week)

@app.route('/submittodoitem', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', data=form_data)
    return 'Data Submitted Successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9001, debug=True)
from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.Python

collenction = db['to-do-list']

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collenction.insert_one(form_data)
    return "Data Submitted Successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000, debug=True)
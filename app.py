import os
2
from flask import Flask, render_template, abort, url_for, json, jsonify
3
import json
4
5
app = Flask(__name__,template_folder='.')
6
7
# read file
8
with open('file.json', 'r') as myfile:
9
    data = myfile.read()
10
11
@app.route("/")
12
def index():
13
    return render_template('index.html', title="page", jsonfile=json.dumps(data))
14
15
16
if __name__ == '__main__':
17
    app.run(debug=True, host='0.0.0.0')
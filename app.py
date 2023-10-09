"""testing cicd changed some commits"""

import json

from flask import Flask, render_template # pylint: disable=invalid-name

app = Flask(__name__,template_folder='.')

with open('file.json', 'r', encoding="utf-8") as myfile:
    data = myfile.read()

@app.route("/")
def index():
    """ it returns the code sample """
    return render_template('index.html', title="page", jsonfile=json.dumps(data))

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

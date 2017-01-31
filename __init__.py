from flask import Flask
from flask import render_template
from datetime import datetime

import nba_py

app = Flask(__name__)


@app. route('/')
def index():
    return render_template('index.html',
                           title="Daily Scores")


if __name__ == '__main__':
    # app.run(threaded=True)
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)

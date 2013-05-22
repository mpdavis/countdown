import os
import time, datetime
from flask import Flask, render_template, redirect, url_for

# Determining the project root.
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# Creating the Flask app object
app = Flask(__name__, static_folder=os.path.join(PROJECT_ROOT, 'static'), static_url_path='/static')


@app.route('/', methods=['GET'])
def index():

    start = datetime.datetime(2013, 5, 20)
    end = datetime.datetime(2013, 6, 10)

    context = {
        'start': time.mktime(start.timetuple()),
        'end': time.mktime(end.timetuple()),
        'now': time.time(),
    }
    import logging
    return render_template('index.html', **context)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

import random
import time
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("Rolling Dice...")
    time.sleep(1)
    print("Values..")
    time.sleep(1)
    val = random.randint(1, 6)
    val = str(val)
    return val

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', debug=True)

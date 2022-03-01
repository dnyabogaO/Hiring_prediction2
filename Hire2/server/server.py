from flask import Flask, request, jsonify, render_template
import pickle

import utils
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello world"



if __name__ == "__main__":
    print("Starting Python Flask Server for salary prediction")
    app.run()
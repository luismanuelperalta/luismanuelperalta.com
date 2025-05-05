
from flask import Flask, render_template, request
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True, port = 3000)

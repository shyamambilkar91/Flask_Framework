from flask import Flask
import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Flask Application'

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=5050)
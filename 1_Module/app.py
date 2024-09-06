from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_Flask():
    return "Hello User,Welcome to Flask Framework...!!"

@app.route('/')
def hello_world():
    return "Hello User, Welcome to the Python & Data Science Class...!!"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5050,debug=True)
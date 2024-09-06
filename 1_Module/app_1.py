from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/hello/<name>')
def hello_Name(name):
    return 'Hello %s, Welcome to the Data Science Class...!!' % name


if __name__=='__main__':
    app.run()
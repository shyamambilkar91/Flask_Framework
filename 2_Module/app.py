from flask import  Flask

app = Flask(__name__)

@app.route('/posting/<post>')
def index(post):
    return "My post is %s" %post

@app.route('/rev/<float:Number>')
def add(Number):
    return "Addition of First Number %f" %Number

if __name__=="__main__":
    app.run()
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    my_dict = {'English':50,'Hindi':75,'Marathi':85, 'Biology':68,'Chemistry':70}
    return render_template('home.html', result = my_dict)


if __name__=="__main__":
    app.run()
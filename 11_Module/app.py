from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 663
app.config['MAIL_USERNAME'] = 'shyamambilkar@gmail.com'
app.config['MAIL_PASSWORD'] = 'Shyam#713'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def index():
    msg = Message("Hello", sender='shyamambilkar91@gmail.com', recipients=['shyamambilkar2@gmail.com'])
    msg.body = 'Hello Flask Message sent from Flask-Mail'
    mail.send(msg)
    return 'sent'


if __name__=="__main__":
    app.run()



# importing libraries
from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'varunpintu23@gmail.com'
app.config['MAIL_PASSWORD'] = '8184869442@vV'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
   
# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
   msg = Message(
                'Hello',
                sender ='yourId@gmail.com',
                recipients = ['varunpintu100@gmail.com']
               )
   msg.body = 'Hello Flask message sent from Flask-Mail'
   mail.send(msg)
   return 'Sent'
   
if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


app = Flask(__name__)
CORS(app)


smtp = smtplib.SMTP(os.environ['HOST'], os.environ['PORT_EMAIL'])
# smtp.connect(os.environ['HOST'], os.environ['PORT_EMAIL'])
smtp.starttls()

email = os.environ['EMAIL']
sender = email
receivers = [email]

smtp.login(sender, os.environ['EMAIL_PASSWORD'])


@app.route('/')
def index():
  return 'Hello'


@app.route('/email', methods=['POST'])
def email():
  if request.method == 'POST':
    data = request.get_json()
    subject = data['subject']
    msg = 'Subject: {}\n\n{}'.format(subject, data['message'])
    smtp.sendmail(sender, receivers, msg)
    smtp.quit()
    return jsonify({
      'status': 200,
      'message': msg
    })

if __name__ == '__main__':
  app.run(debug=False)

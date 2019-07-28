from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


app = Flask(__name__)
CORS(app)


smtp = smtplib.SMTP(os.getenv('HOST'), os.getenv('PORT'))
smtp.connect(os.getenv('HOST'), os.getenv('PORT'))
smtp.starttls()

email = os.getenv('EMAIL')
sender = email
receivers = [email]

smtp.login(sender, os.getenv('EMAIL_PASSWORD'))


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
    return jsonify({
      'status': 200,
      'message': msg
    })

if __name__ == '__main__':
  app.run(debug=False)
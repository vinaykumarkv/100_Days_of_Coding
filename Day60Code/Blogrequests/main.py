from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
import requests
import sys

sys.path.insert(1, '/Users/vinay/PycharmProjects')
import creds

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use appropriate port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = creds.gmailuser
app.config['MAIL_PASSWORD'] = creds.gmailpassword
app.config['MAIL_DEFAULT_SENDER'] = creds.gmailuser
to_user = creds.toemailID

mail = Mail(app)


@app.route('/')
@app.route('/home/')
def home():
	response = requests.get("https://api.npoint.io/96b730aa2fba47ec6019")
	posts = response.json()
	return render_template('index.html', posts=posts)


@app.route('/about/')
def about():
	return render_template('about.html')


@app.route('/contact/')
def contact():
	return render_template('contact.html')


@app.route('/post/<id>')
def post_id(id):
	response = requests.get("https://api.npoint.io/96b730aa2fba47ec6019")
	posts = response.json()
	return render_template("post.html", id=id, posts=posts)


@app.route('/submit_details', methods=['POST'])
def submit_details():
	name = request.form['name']
	email = request.form['email']
	message = request.form['message']
	phone = request.form['phone']

	msg = Message('New Message from Website', recipients=[f'{to_user}'])
	msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}  mobile number-{phone}'
	mail.send(msg)

	message= 'Details submitted successfully. Thank you!'
	return render_template('contact.html', message=message)


# Redirect '/' to '/home/'
@app.route('/')
def root():
	return redirect(url_for('home'))


if __name__ == "__main__":
	app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587  # Use appropriate port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'

mail = Mail(app)

@app.route('/')
@app.route('/home/')
def home():
	return render_template('index.html')


@app.route('/submit_details', methods=['POST'])
def submit_details():
	name = request.form['name']
	email = request.form['email']
	message = request.form['message']

	msg = Message('New Message from Website', recipients=['your@example.com'])
	msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
	mail.send(msg)

	return 'Details submitted successfully. Thank you!'


# Redirect '/' to '/home/'
@app.route('/')
def root():
	return redirect(url_for('home'))


if __name__ == "__main__":
	app.run(debug=True)

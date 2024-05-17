from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)


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

# Redirect '/' to '/home/'
@app.route('/')
def root():
	return redirect(url_for('home'))


if __name__ == "__main__":
	app.run(debug=True)

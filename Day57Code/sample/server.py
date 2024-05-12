from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__, static_url_path='/static')
agify_url= "https://api.agify.io?name="
gender_url = "https://api.genderize.io?name="
blog_api = "https://api.npoint.io/008169d14c71f9cf86f7"
@app.route("/")
def home():
	num = random.randint(1, 10)
	current_year = datetime.datetime.now().year
	return render_template("index.html", num=num, current_year=current_year)

@app.route("/guess/<text>")
def guess(text):
	response = requests.get(agify_url+f"{text.title()}")
	age = response.json()['age']
	response = requests.get(gender_url + f"{text.title()}")
	gender = response.json()['gender']
	return render_template("guess.html", name=text, age=age, gender=gender)


@app.route("/blog")
def blog():
	response = requests.get(blog_api)
	all_posts = response.json()
	return render_template("blog.html", posts=all_posts)

if __name__ == "main":
	app.run(debug=True)

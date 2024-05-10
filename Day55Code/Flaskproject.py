from flask import Flask

app = Flask(__name__)


def make_underline(func):
	def wrapper(*args, **kwargs):
		content = func(*args, **kwargs)
		return f"<u>{content}</u>"

	return wrapper



def make_emphasis(func):
	def wrapper(*args, **kwargs):
		content = func(*args, **kwargs)
		return f"<em>{content}</em>"

	return wrapper



def make_bold(func):
	def wrapper(*args, **kwargs):
		content = func(*args, **kwargs)
		return f"<b>{content}</b>"

	return wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underline
def hello():
	return ("<h1>Hello, World!</h1>"
	        "<p> I am placing a cute Kitty cat down here,</p>"
	        '<iframe src="https://giphy.com/embed/xMLhn5LOHoDio" width="480" height="241" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cute-kitten-xMLhn5LOHoDio">via GIPHY</a></p>')

@app.route("/bye")
def bye():
	return "Bye!"

@app.route("/<name>/<int:number>")
def greet(name, number):
	return f"Hello there, {name+12} + {number}"


if __name__ == "main":
	app.run(debug=True)

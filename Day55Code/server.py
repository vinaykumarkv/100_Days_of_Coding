from flask import Flask
import random
app = Flask(__name__)

def generate_random_number():
	return random.randint(0, 9)
random_number = generate_random_number()

def make_bold(func):
	def wrapper(*args, **kwargs):
		content = func(*args, **kwargs)
		return f"<b>{content}</b>"

	return wrapper


@app.route("/")
@make_bold
def hello():
	return ('<h1>Guess a number between 0 and 9</h1>'
	        '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWExc28zY2VwdGlkOTh4MjhtNWg1YXl6ejlheHp0bWVhdzJjemJjYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif" >')


def guess_number(guess):
	if guess == random_number:
		return ('<h1 style="color: green;">Your guess is right! congrats.</h1>'
		        '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXoxd2JidnB3amw4cXUxeGl1a21hdW1iNzlhbGl2NGkyY3RwMHczeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZFFVNwIbjsKtP3lHYK/giphy.gif">')
	elif guess > random_number:
		return ('<h1 style="color: red;"> Your guess is higher than expected number, try again</h1>'
		        '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmhkZHozcGx6NmM4cWluanlvb3R2MTlxeGJuNGZkaWFkMHhrcGZ3ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jUcETcDU7LuzeJCqyn/giphy.gif">')
	elif guess < random_number:
		return ('<h1 style="color: yellow;"> Your guess is lower than expected number, try again</h1>'
		        '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmhkZHozcGx6NmM4cWluanlvb3R2MTlxeGJuNGZkaWFkMHhrcGZ3ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jUcETcDU7LuzeJCqyn/giphy.gif">')

@app.route("/<int:number>")
def guesser(number):
	return guess_number(number)


if __name__ == "main":
	app.run(debug=True)

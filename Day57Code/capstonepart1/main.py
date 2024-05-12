from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/008169d14c71f9cf86f7")
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route('/post/<id>')
def post_id(id):
    response = requests.get("https://api.npoint.io/008169d14c71f9cf86f7")
    posts = response.json()
    return render_template("post.html", id=id, posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

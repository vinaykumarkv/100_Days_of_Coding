from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = StringField('Email', render_kw={"size": 30}, validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)], render_kw={"size": 30} )
    submit = SubmitField('Login')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "some secret string"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


@app.route('/')
def root():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

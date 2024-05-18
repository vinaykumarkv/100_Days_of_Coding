from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)




class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open_time = StringField('Open', validators=[DataRequired()])
    close_time = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕')], validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=[('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪')], validators=[DataRequired()])
    power = SelectField('Power', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST' and form.validate_on_submit():
        cafe_name = form.cafe_name.data
        location = f'=HYPERLINK("{form.location.data}", "Link")'
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data

        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([cafe_name, location, open_time, close_time, coffee, wifi, power])

        return render_template('add.html', form=form, success_message="Cafe data added successfully!")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

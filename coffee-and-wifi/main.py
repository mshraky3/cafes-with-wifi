from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , SelectField
from wtforms.validators import DataRequired , URL
import csv


app = Flask(__name__)
app.secret_key = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()] )
    location = StringField('Location on google maps (URL)' , validators=[DataRequired() , URL()])
    open = StringField('opening time' , validators=[DataRequired()])
    closing = StringField('closing time' , validators=[DataRequired()])
    rating = SelectField('coffee rating' , validators=[DataRequired()], choices=("☕", "☕☕" ,"☕☕☕" ,"☕☕☕☕" ,"☕☕☕☕☕"))
    wifi = SelectField ('wifi' , validators=[DataRequired()] , choices=("⭐", "⭐⭐" ,"⭐⭐⭐" ,"⭐⭐⭐⭐" ,"⭐⭐⭐⭐⭐"))
    power = SelectField('power' , validators=[DataRequired()] , choices=("⚡", "⚡⚡" ,"⚡⚡⚡" ,"⚡⚡⚡⚡" ,"⚡⚡⚡⚡⚡") )
    submit = SubmitField('submit')

# Exercise:


# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields



# make coffee/wifi/power a select element with choice of 0 to 5.


#e.g. You could use emojis ☕️/💪/✘/🔌

# make all fields required except submit

# use a validator to check that the URL field has a URL entered.


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add' ,  methods=["GET" , "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv'  , "a", newline='', encoding='utf-8') as csv_file:
           w = csv.writer(csv_file)
           w.writerow([ form.cafe.data , form.location.data  , form.open.data, form.closing.data ,form.rating.data ,form.wifi.data ,form.power.data ])
    return render_template('add.html', form=form)


@app.route('/cafes' )
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

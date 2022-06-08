from flask import Flask, render_template
from tinydb import TinyDB, Query

app = Flask(__name__)

@app.route("/")
def root(user='Philo'):
    user = user or 'Shalabh'
    return render_template('index.html', user=user)


@app.route('/home')
def home():
    return render_template('home.html')
 
@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/form')
def form():
    return render_template('form.html')

db = TinyDB('db.json')

app.run()




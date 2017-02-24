from flask import Flask, session

from flask import render_template
from flask import request,redirect
from flask import make_response, url_for
import MySQLdb


conn = MySQLdb.connect(host= "Timelesscode.mysql.pythonanywhere-services.com",
                  user="Timelesscode",
                  passwd="bryan",
                  db="Timelesscode$posts")


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def hello_world():
    session['username'] = " Guest"
    return render_template("home.html")

@app.route("/posts")
def home():
    return render_template("posts.html")

@app.route("/posts", methods=['POST'])
def postsg():
    text = request.form['content']
    processed_text = text

    return  redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    return render_template("profile.html",user = session['username'])


@app.route("/profile", methods=['POST'])
def profileg():
    text = request.form['text']
    processed_text = text
    session['username'] = processed_text
    return  redirect(url_for('home'))

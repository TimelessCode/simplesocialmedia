from flask import Flask, session

from flask import render_template
from flask import request,redirect
from flask import make_response, url_for


app = Flask(__name__, template_folder='Postr/templates',static_folder='Postr/static')
app.secret_key=b'tk9\xab\xe5\xfb\xcc\xd6k'


@app.route('/')
def hello_world():
    session['username'] = " Guest"
    return render_template("home.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route("/posts", methods=['POST'])
def postsg():
    text = request.form['content']
    processed_text = text
    return  redirect(url_for('posts'))


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

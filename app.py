from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", page_name="index")

@app.route('/research')
def research():
    return render_template("research.html", page_name="research")

@app.route('/design')
def design():
    return render_template("design.html", page_name="design")
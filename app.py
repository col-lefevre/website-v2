from flask import Flask, render_template, url_for

app = Flask(__name__)

nav_links = {"index": "About", "research": "Research", "cv": "CV", }

@app.route('/')
def index():
    return render_template("index.html", page_name="index")
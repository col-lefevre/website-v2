from flask import Flask, render_template, url_for
import dataParse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", page_name="index")

@app.route('/research.html')
def research():
    return render_template("research.html", page_name="research", project_data=dataParse.researchDataParse())

@app.route('/design.html')
def design():
    return render_template("design.html", page_name="design")
from flask import Flask, render_template, url_for
import dataParse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", page_name="index")

@app.route('/research.html')
def research():
    return render_template("research.html", page_name="research")

@app.route('/abortion_activism.html')
def abortion_activism():
    return render_template("research_project.html", page_name="research", project=dataParse.getProject(1))

@app.route('/reflection_bereavement.html')
def reflection_bereavement():
    return render_template("research_project.html", page_name="research", project=dataParse.getProject(2))

@app.route('/cooking_experiences.html')
def cooking_experiences():
    return render_template("research_project.html", page_name="research", project=dataParse.getProject(3))

@app.route('/design.html')
def design():
    return render_template("design.html", page_name="design")
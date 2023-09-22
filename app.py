from flask import Flask, render_template, url_for
import dataParse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", page_name="index")

@app.route('/research.html')
def research():
    return render_template("research.html", page_name="research", projects=dataParse.getProjectSummaries())

# Manually match main.csv stub and id
@app.route('/abortion_activism.html')
def abortion_activism():
    return render_template("research_project.html", page_name="research", project=dataParse.getProjectData(1))

# Manually match main.csv stub and id
@app.route('/reflection_grief.html')
def reflection_bereavement():
    return render_template("research_project.html", page_name="research", project=dataParse.getProjectData(2))

# Manually match main.csv stub and id
@app.route('/cooking_experiences.html')
def cooking_experiences():
    return render_template("research_project.html", page_name="research", project=dataParse.getProjectData(3))
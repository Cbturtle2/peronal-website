from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/proj/distinction')
def distinction():
    return render_template('proj/distinction.html')

@app.route('/proj/LAACESProgManager')
def laacesProgManager():
    return render_template('proj/laacesProgManager.html')

@app.route('/proj/LAACESProgAssistant')
def laacesProgAssistant():
    return render_template('proj/laacesProgAssistant.html')

@app.route('/assets/<path:path>', methods=['GET'])
def _send_static(path):
    return send_from_directory('assets', path)
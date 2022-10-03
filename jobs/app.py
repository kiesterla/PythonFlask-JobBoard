from flask import Flask, render_template

app = Flask(__name__)
@app.route('/jobs')
@app.jobs('/')
def jobs():
    return render_template('index.html')
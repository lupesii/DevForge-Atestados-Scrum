from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html"),200

@app.route("/header")
def header():
    return render_template('header.html')

app.run(debug=True, use_reloader=True)
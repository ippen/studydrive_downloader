# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route("/", methods=["GET"])

def adder_page():
    return render_template("index.html")

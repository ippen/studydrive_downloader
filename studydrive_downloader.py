# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, url_for
from processing import counter_increase, get_counter, ensure_https_www_prefix, is_valid_url, get_lol_url

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route("/", methods=["GET", "POST"])

def adder_page():
    error_msg = ""
    if request.method == "POST":
        #return render_template("Result-Page-1.html")

        try:
            url = request.form["Studydrive Link"]
        except:
            url = None

        url = ensure_https_www_prefix(url)
        if url is not None and is_valid_url(url):
            result = get_lol_url(url)
            counter_increase()
            return render_template("Result-Page.html", result=result, counter=get_counter())
        else:
            error_msg = "Error: The provided Link is not a Studydrive File Link (e.g. \"studydrive.net/en/doc/doc_name/123456\")"

    return render_template("index.html", error_msg=error_msg, counter=get_counter())

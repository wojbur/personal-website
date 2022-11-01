import os
from flask import Flask, render_template, send_from_directory, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def sumbit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect("thankyou.html")
    else:
        return 'somthing went wrong'
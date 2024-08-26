from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<museum_name>/<code>")
def pages(museum_name, code):
    return render_template(f"/{museum_name}/{code}.html")

app.run(host='0.0.0.0',port=80,debug=True)
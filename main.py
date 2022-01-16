from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    return "<h1>HEllo Earth!</h1>"
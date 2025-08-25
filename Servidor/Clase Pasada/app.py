from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/sensor", methods=['POST'])
def json_Date():
    data =request.json
    name =data.get("luxometro")
    age =data.get("123")
    return print(name, age, "ok")
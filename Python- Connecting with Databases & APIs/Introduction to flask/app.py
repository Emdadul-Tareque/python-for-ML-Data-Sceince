from flask import Flask
from flask import request as req 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/h")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/test")
def test():
    a = 10 +5
    return f"The sum:{a}"

@app.route("/test/t")
def test1():
    data = req.args.get("q")
    return f"The input is: {data}"  
if __name__=="__main__":
    app.run(host="0.0.0.0")

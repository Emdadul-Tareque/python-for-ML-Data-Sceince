from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/math", methods=["POST"])
def math_operation():
    ops = request.form['operation']
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    if (ops == 'add'):
        res = num1 + num2
        result = f"the sum of {num1} and {num2} is {res}"
    if (ops == 'subtract'):
        res = num1 - num2
        result = f"the substraction of {num1} and {num2} is {res}"
    if (ops == 'multiply'):
        res = num1 * num2
        result = f"the multiplication of {num1} and {num2} is {res}"
    if (ops == 'divide'):
        res = num1 / num2
        result = f"the divition of {num1} and {num2} is {res}"

    return render_template('result.html', result = result)


if __name__=="__main__":
    app.run(host="0.0.0.0")

from flask import Flask
from flask import request
app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'


@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(num1, operation, num2):


    if operation == "add":
        result = (f"{num1 + num2}")

    elif operation == "subtract":
        result = (f"{num1 - num2}")

    elif operation == "multiply":
        result = (f"{num1 * num2}")

    elif operation == "divide":
        result = (f"{num1 / num2}")

    else:
        result = "Invalid Operation"


    return result



@app.route('/search')
def search():

    query = request.args.get('q', '')

    category = request.args.get('category', 'all')

    return f'Searching for "{query}" in category: {category}'


if __name__ == '__main__':
    app.run(debug=True)
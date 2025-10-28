from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect




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




@app.route('/basic')
def basic():
    return render_template('basic.html')




@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)




@app.route('/inventory')
def inventory():
    inventory_items = ['yates', 'jimmy', 'e']
    return render_template('inventory.html', inventory = inventory_items)




@app.route('/test/<message>')
def test(message):
    return render_template('test.html', message = message)

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username = username)




@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Here you would typically save this data or send an email

        return redirect(url_for('thankyou', name=name, message=message))

    return render_template('contact.html')





if __name__ == '__main__':
    app.run(debug=True)
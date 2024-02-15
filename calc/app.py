from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add_route():
    """Add a and b params."""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(add(a,b))

@app.route('/sub')
def sub_route():
    """Subtract a and b params."""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a,b))

@app.route('/mult')
def mult_route():
    """Multiply a and b params"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a,b))

@app.route('/div')
def div_route():
    """Divide a and b params"""
    
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a,b))
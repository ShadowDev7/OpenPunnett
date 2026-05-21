from flask import Flask, render_template, request
from cli.program import calculate_punnett_square
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    parent1 = request.form['parent1']
    parent2 = request.form['parent2']
    results = calculate_punnett_square(parent1, parent2)
    return render_template('results.html', results=results)

from flask import Flask, render_template
from utils.fetch_data import fetch_data



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cats')
def cats():
    cats_url = 'https://api.thecatapi.com/v1/breeds'
    data = fetch_data(cats_url)
    number = len(data)
    return render_template('cats.html', data = data, number = number)


if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 9000)


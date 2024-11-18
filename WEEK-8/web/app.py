from flask import Flask, render_template
from utils.fetch_data import fetch_data
from pprint import pprint



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
    data = [ {**cat, 'url': f'https://cdn2.thecatapi.com/images/{cat.get('reference_image_id')}.jpg'} for cat in data]
    new_data = []
    for cat in data:
        cat['url'] = f'https://cdn2.thecatapi.com/images/{cat.get('reference_image_id')}.jpg'
        new_data.append(cat)
    pprint(new_data)
    number = len(new_data)
    return render_template('cats.html', data = new_data, number = number)

@app.route('/api/v1/cats')
def cats_api():
    cats_url = 'https://api.thecatapi.com/v1/breeds'
    data = fetch_data(cats_url)
    new_data = []
    for cat in data:
        mn, mx = cat['life_span'].split(' - ')
        average_life_span = (int(mn) + int(mx)) / 2
        lowest, heighest = cat['weight']['metric'].split(' - ')
        average_weight = (int(lowest) + int(heighest)) / 2
        dct = {
            'country':cat['origin'],
            'description':cat['description'],
            'image':f'https://cdn2.thecatapi.com/images/{cat.get('reference_image_id')}.jpg',
            'life_span': average_life_span,
            'weigth': average_weight,
            "temperament": cat['temperament']
        }
        new_data.append(dct)
    return new_data
    '''
    "country": "Egypt",
"description": "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.",
"image": "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg",
"life_span": 14.5,
"name": "Abyssinian",
"temperament": "Active, Energetic, Independent, Intelligent, Gentle",
"weight": 4
    
    '''
    


if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 9000)


from flask import Flask, render_template
from mysql.connector import connect


app = Flask(__name__)


db = connect(
    host ='localhost',
    user = 'root',
    password = 'root',
    database = 'blog_db'
    
)
cursor = db.cursor()
print('Cursor', 'you are connected to a MySQL server')


@app.route('/test')
def test():
    return 'test'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/blogs/add')
def add_blog():
    return render_template('add-blog.html')



if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = '5000')
    
    
'''

CRUD => Creating/POST
R: Read
U: Update/Modify
D: Deleting / Removing

INSER INTO blogs(id, title, subtitle, category, content) VALUES (1, 'Title one ', 'Subtitle 1', 'web', 'We love bloging. Really we enjoi' );


'''
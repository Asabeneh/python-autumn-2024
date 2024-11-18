from flask import Flask, render_template, jsonify, request, redirect, url_for
from mysql.connector import connect
import os
from utils.categories import blog_categories

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'


db = connect(
    host ='localhost',
    user = 'root',
    password = 'root',
    database = 'blog_db'
    
)
cursor = db.cursor()
print('Cursor', 'you are connected to a MySQL server') 
print(cursor)

def create_table():
    cursor.execute('DROP TABLE IF EXISTS blogs')
    cursor.execute('''CREATE TABLE IF NOT EXISTS blogs (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        subtitle VARCHAR(255),
        category VARCHAR(255),
        content TEXT,
        tags TINYTEXT,
        cover_img VARCHAR(255) DEFAULT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
    
# create_table()

users = [
    {
        'first_name': 'John',
        'role': 'Fulstack',
        'age': 25,
        'email': 'john@gmail.com',
        'gender': 'male'
    },
    {
        'first_name': 'David',
        'role': 'Fulstack',
        'age': 24,
        'email': 'david@gmail.com',
        'gender': 'male'
    },
    {
        'first_name': 'Marta',
        'role': 'Fulstack',
        'age': 22,
        'email': 'marta@gmail.com',
        'gender': 'female'
    }
]


@app.route('/users')
def test():
    return jsonify(users)


@app.route('/')
def home():
    return render_template('index.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blogs')
def blogs():
    cursor.execute("SELECT * FROM blogs")
    blogs = cursor.fetchall()
    formatatted_blogs = []
    for blog in blogs:
         item = {
         'id': blog[0],
         'title':blog[1],
         'subtitle':blog[2],
         'category':blog[3],
         'content':blog[4],
         'tags':blog[5],
         'cover_img':blog[6],
         'created_at':blog[7]
         }
         formatatted_blogs.append(item)
    return render_template('blogs.html', data = formatatted_blogs)


@app.route('/blogs/add', methods = ['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        form = request.form 
        title = form.get('title')
        subtitle = form.get('subtitle')
        category = form.get('category')
        content = form.get('content')
        tags = form.get('tags')
        file = request.files.get('cover_img')
        filename = ''
        if file:
            filename = file.filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
        
        cursor.execute("INSERT INTO blogs (title, subtitle, category, content, tags, cover_img) VALUES (%s, %s, %s, %s, %s, %s)",(title, subtitle, category, content, tags, filename))
        db.commit()
      
        print(form, title, subtitle, category, content)
        print('this is inside the post method')
        return redirect(url_for('blogs'))
        
    elif request.method == 'GET':
        print('this is inside the get method')
        return render_template('add-blog.html', blog_categories = blog_categories)
    else:
        pass
    
@app.route('/blogs/delete/<id>')
def delete_blog(id):
    cursor.execute('DELETE FROM blogs WHERE id = %s', (id,))
    db.commit()
    return redirect(url_for('blogs'))

@app.route('/blogs/edit/<id>', methods = ['GET', 'POST'])
def edit_blog(id):
    
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        subtitle = form.get('subtitle')
        category = form.get('category')
        content = form.get('content')
        tags = form.get('tags')
        file = request.files.get('cover_img')
        filename = ''
        if file and file.filename:
            filename = file.filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
        else:
            cursor.execute('SELECT * FROM blogs WHERE id = %s', (id,))
            item = cursor.fetchone()
            filename = item[6]
        cursor.execute('UPDATE blogs SET title = %s, subtitle = %s, category = %s, content = %s, tags = %s, cover_img = %s WHERE id = %s', (title, subtitle, category, content, tags, filename, id))
        db.commit()
        return redirect(url_for('blogs'))
    cursor.execute('SELECT * FROM blogs WHERE id = %s', (id,))
    item = cursor.fetchone()
    blog = {
        'id': item[0],
         'title':item[1],
         'subtitle':item[2],
         'category':item[3],
         'content':item[4],
         'tags':item[5],
          'cover_img':item[6]
    }
    return render_template('edit-blog.html', blog = blog, categories = blog_categories)

@app.route('/blogs/<id>', methods = ['GET'])
def blog(id):
    cursor.execute('SELECT * FROM blogs WHERE id = %s', (id,))
    item = cursor.fetchone()
    blog = {
        'id': item[0],
         'title':item[1],
         'subtitle':item[2],
         'category':item[3],
         'content':item[4],
         'tags':item[5].strip().lower().split(','),
        'cover_img':item[6],
        'created_at':item[7]
    }
    return render_template('blog.html', blog = blog)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)


'''

CRUD => Creating/POST
R: Read GET
U: Update/Modify PUT
D: Deleting / Removing DELETE

INSER INTO blogs(id, title, subtitle, category, content) VALUES (1, 'Title one ', 'Subtitle 1', 'web', 'We love bloging. Really we enjoi' );


'''


'''
CRUD:
- GET - Reading 
- POST - Creating
- PUT - UPDATE
- DELETE - DELETE

'''
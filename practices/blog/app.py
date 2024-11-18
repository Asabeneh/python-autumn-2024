from flask import Flask, render_template, request, redirect,url_for
from mysql.connector import connect
import os
from utils import categories
import re 


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

# def create_database(db_name):
#     cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
# create_database('python_sql_test_db')
# cursor.execute('USE python_sql_test_db')

def show_tables(db_name, table_name):
    cursor.execute(f'USE {db_name}')
    cursor.execute(f'SELECT * FROM {table_name}')


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
    cursor.execute("SELECT * FROM blogs")
    items = cursor.fetchall()
    blogs = list( map(lambda item : {
        'id': item[0],
         'title':item[1],
         'subtitle':item[2],
         'category':item[3],
         'content':item[4],
         'tags':item[5],
         'cover_img':item[6],
         'created_at':item[7]
    }, items))
    return render_template('blogs.html', blogs = blogs)
@app.route('/blogs/<id>', methods = ['GET'])
def blog(id):
    cursor.execute('SELECT * FROM blogs WHERE id = %s', (id,))
    item = cursor.fetchone()
    print(item)
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
        return redirect('blogs')
    return render_template('add-blog.html', categories = categories.blog_categories)

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
    return render_template('edit-blog.html', blog = blog, categories = categories.blog_categories)

@app.route('/blogs/delete/<id>')
def delete_blog(id):
    cursor.execute('DELETE FROM blogs WHERE id = %s', (id,))
    db.commit()
    return redirect(url_for('blogs'))

@app.route('/blogs/filter')
def filter_blogs():
    try:
        search_term = ''
        title = request.args.get('title')
        description = request.args.get('description')
        regex_title = re.compile(f'.*{title}.*', re.IGNORECASE)
        regex_description = re.compile(f'.*{title}.*', re.IGNORECASE)
        filter_dict = {'title':regex_title}
        
        if title:
            search_term = title
            filter_dict['title'] = regex_title
            
        # jobs = [job for job in db.jobs.find({'title':{'$regex':title, '$options':'i'}})]
        # {'title':regex}
        blogs = [blog for blog in db.blogs.find(filter_dict)]
        return render_template('blogs.html', blogs=blogs, number=len(list(blogs)), search_term = search_term)
    except Exception as e:
        return render_template('not-found.html')
    



if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = '5000')
    
    
'''

CRUD => Creating/POST
R: Read
U: Update/Modify
D: Deleting / Removing

INSER INTO blogs(id, title, subtitle, category, content) VALUES (1, 'Title one ', 'Subtitle 1', 'web', 'We love bloging. Really we enjoi' );


'''
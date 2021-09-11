import sqlite3
import logging
import os
from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

count = 0
db_file= 'database.db'

def db_connection_count():
    global count
    count+=1
    
# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    try:
        connection = sqlite3.connect('database.db')
        connection.row_factory = sqlite3.Row
        db_connection_count()
    except:
        app.logger.info("Error - Missing {}".format(db_file))
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      app.logger.info("requests a(n) non-existent/existing post(s)")
      return render_template('404.html'), 404
    else:
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/healthz')
def healthcheck():
    if os.path.exists(db_file):
        return jsonify({"result": "OK - healthy"})
    else:
        return jsonify({"result": "Error - Missing {}".format(db_file)}), 500

@app.route('/metrics')
def metrics():
    con = get_db_connection()
    posts_count = con.execute('SELECT * FROM posts').fetchall()
    con.close()
    response = app.response_class(
            response=json.dumps({"status":"success","db_connection_count": count,"post_count": str(len(posts_count))}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return response

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()

            return redirect(url_for('index'))

    return render_template('create.html')

def initialize_logger():
    log_level = os.getenv("LOGLEVEL", "DEBUG").upper()
    log_level = (
        getattr(logging, log_level)
        if log_level in ["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING",]
        else logging.DEBUG
    )

    logging.basicConfig(
        format='%(levelname)s:%(name)s:%(asctime)s, %(message)s',
                level=log_level,
    )

if __name__ == "__main__":
    initialize_logger()
    app.run(host='0.0.0.0', port='3111')

# app.py
from flask import Flask, render_template, redirect, url_for, request, session
from models import db, User, Post, Comment, create_all_tables
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create all tables if they don't exist
create_all_tables(app)


@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=10, error_out=False)
    return render_template('home.html', posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #hashed_password = generate_password_hash(password)
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user.password == password: #and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/post', methods=['POST'])
def post():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    title = request.form['title']
    content = request.form['content']
    user_id = session['user_id']
    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/comment', methods=['POST'])
def comment():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    content = request.form['content']
    post_id = request.form['post_id']
    user_id = session['user_id']
    comment = Comment(content=content, post_id=post_id, user_id=user_id)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

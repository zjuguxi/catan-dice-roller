from flask import render_template, redirect, url_for, session
from datetime import datetime
from . import main
from app.forms import PostForm

@main.route('/', methods = ['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        session['post'] = form.post.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time = datetime.utcnow(), form = form, post = session.get('post'))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
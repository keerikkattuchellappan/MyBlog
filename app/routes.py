from app import blog
from flask import render_template
from app.forms import LoginForm


@blog.route('/')
@blog.route('/index')
def index():
    user = {'username': 'Keerikkattu Chellappan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@blog.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title ='Sign In', form = form)

